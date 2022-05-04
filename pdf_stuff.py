import PyPDF2
import sys

def main():
  watermark_pdf = sys.argv[1]
  pdf = sys.argv[2]

  watermark = PyPDF2.PdfFileReader(watermark_pdf)

  reader = PyPDF2.PdfFileReader(pdf)
  writer = PyPDF2.PdfFileWriter()

  for page in reader.pages:
    page.mergePage(watermark.pages[0])
    writer.addPage(page)

  with open(sys.argv[3], 'wb') as new_pdf:
    writer.write(new_pdf)

if __name__ == '__main__':
  main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
