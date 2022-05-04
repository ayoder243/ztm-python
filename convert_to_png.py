import sys
from pathlib import Path
from PIL import Image

def main():
  try:
    current_dir = sys.argv[1]
    new_dir = sys.argv[2]
  except IndexError:
    print('please enter directories as arguments when calling script')
  else:
    if Path(current_dir).is_dir():
      try:
       Path(new_dir).mkdir(parents=True, exist_ok=True)
      except:
        print('enter an appropriate directory')
      else:
        contents = Path(current_dir).glob('**/*')
        images = [x for x in contents if x.is_file()]

        for image in images:
          image = str(image).split('/')[1]
          img = Image.open(f'{current_dir}/{image}')
          new_filename = image[:-3] + '.png'
          img.save(f'{new_dir}/{new_filename}', 'png')
    else:
      print('enter an existing dir of images')


if __name__ == '__main__':
  main()
