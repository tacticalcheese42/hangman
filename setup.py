import os

def setup(level):
  select = '>'
  place = ' '
  start_screen = '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
    {a}'''"\033[32m"'''easy'''"\033[0m"'''
    {b}'''"\033[33m"'''Medium'''"\033[0m"'''
    {c}'''"\033[33m"'''Hard'''"\033[0m"'''
    {d}'''"\033[31m"'''Extreme'''"\033[0m"'''
    {e}'''"\033[31m"'''INSANE'''"\033[0m"
  while True:
    if level == 0:
      print(start_screen.format(a=select, b=place, c=place, d=place, e=place))
    if level == 1:
      print(start_screen.format(a=place, b=select, c=place, d=place, e=place))
    if level == 2:
      print(start_screen.format(a=place, b=place, c=select, d=place, e=place))
    if level == 3:
      print(start_screen.format(a=place, b=place, c=place, d=select, e=place))
    if level == 4:
      print(start_screen.format(a=place, b=place, c=place, d=place, e=select))
    modifier = input(
      'Use \'w\' and \'s\' to change difficulty  and \'e\' to select\n>')
    os.system('clear')
    if modifier == 's':
      level += 1
      if level == 5:
        level = 0
    elif modifier == 'w':
      level -= 1
      if level == -1:
        level = 4
    elif modifier == 'e':
      return (level)
