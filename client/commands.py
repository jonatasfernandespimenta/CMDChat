import utils.globals as g
from PIL import ImageGrab, Image
import sys
from utils.colors import setColor

def printscreen(sendMessage):
  im = ImageGrab.grabclipboard()
  im.save('print.png','PNG')

  image_path = 'print.png'
  img = Image.open(image_path)

  # resize the image
  width, height = img.size
  aspect_ratio = height/width
  new_width = 120
  new_height = aspect_ratio * new_width * 0.55
  img = img.resize((new_width, int(new_height)))
  # new size of image
  # print(img.size)

  # convert image to greyscale format
  img = img.convert('L')

  pixels = img.getdata()

  # replace each pixel with a character from array
  chars = ["B","S","#","&","@","$","%","*","!",":",".","/","|","█"]
  new_pixels = [chars[pixel//25] for pixel in pixels]
  new_pixels = ''.join(new_pixels)

  # split string of chars into multiple strings of length equal to new width and create a list
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = "\n".join(ascii_image)
  print(ascii_image)
  sendMessage(ascii_image)

  # write to a text file.
  with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)

def commands(text, sendMessage, clear):
  command = text.replace("/", "")
  if(command == 'nf'):
      if(g.notify == False):
          g.notify = True
      else:
          g.notify = False
      print('Notifications enabled: ', str(g.notify))
  if(command == 'cls'):
    print('\n' * 100)

  if(command == 'print'):
    printscreen(sendMessage)

  if('color' in command):
    if(' ' in command):
      color = text.split(' ')[1]
      setColor(color)
    setColor(text)

  if(command == 'clear'):
    clear()

  if('changeName' in command):
    if(' ' in text):
      newName = text.split(' ')[1]
      g.username = newName
      print('Your username is now: ' + g.username)
    else:
      print('Please enter a new username')
