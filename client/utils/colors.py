import os

def setColor(color):
  print(color)
  if(color == '/color'):
    print('\n')
    print('To set a color, use the following format:')
    print('/color <background color code><text color code>')
    print('Example: /color 0A')
    print('To see a list of colors, use the following command:')
    print('/color list')

  elif(color == 'list'):
    print('\n')
    listColors()

  elif(len(color) == 2):
    os.system('color ' + color)

def listColors():
  print('----------------------------------------------')
  print('|     Color Name      |      Color Code      |')
  print('----------------------------------------------')
  print('|     black           |          0           |')
  print('|     blue            |          1           |')
  print('|     green           |          2           |')
  print('|     cyan            |          3           |')
  print('|     red             |          4           |')
  print('|     magenta         |          5           |')
  print('|     brown           |          6           |')
  print('|     light gray      |          7           |')
  print('|     dark gray       |          8           |')
  print('|     light blue      |          9           |')
  print('|     light green     |          A           |')
  print('|     light cyan      |          B           |')
  print('|     light red       |          C           |')
  print('|     light magenta   |          D           |')
  print('|     yellow          |          E           |')
  print('|     white           |          F           |')
  print('----------------------------------------------')
