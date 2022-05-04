import requests
from bs4 import BeautifulSoup
import pprint
from sys import argv

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(all_links, all_subtext):
  hn = []
  page = 0
  while page < len(all_links):
    for idx, item in enumerate(all_links[page]):
      title = all_links[page][idx].getText()
      href = all_links[page][idx].get('href', None)
      vote = all_subtext[page][idx].select('.score')
      if len(vote):
        points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
          hn.append({'title': title, 'link': href, 'votes': points})
    page += 1
  return hn

def scrape_all_pages(num_pages):
  all_links = []
  all_subtext = []
  for page in num_pages:
    res = requests.get(f'https://news.ycombinator.com/news?p={page}')
    soup = BeautifulSoup(res.text, 'html.parser')
    all_links.append(soup.select('.titlelink'))
    all_subtext.append(soup.select('.subtext'))
  return all_links, all_subtext

def main():
  links, subtext = scrape_all_pages(argv[1])

  pprint.pprint(sort_stories_by_votes(create_custom_hn(links, subtext)))

if __name__ == '__main__':
  main()
