
def setup(level):
  start_screen=[
    '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
    >Easy
     Medium
     Hard
     Extreme
     Insane''',    '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
     Easy
    >Medium
     Hard
     Extreme
     Insane''',    '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
     Easy
     Medium
    >Hard
     Extreme
     Insane''',    '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
     Easy
     Medium
     Hard
    >Extreme
     Insane''',    '''    HANGMAN
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------
    select difficulty:
    
     Easy
     Medium
     Hard
     Extreme
    >Insane'''
  ]
  while True:
    print(start_screen[level])
    modifier=str(input("Use 'w' and 's' to change difficulty  and 'e' to select\n>"))
    print('\n'*15)
    if modifier == 's':
      level+=1
      if level == 5:
        level=0
    elif modifier == 'w':
      level-=1
      if level == -1:
        level = 4
    elif modifier == 'e':
      return(level)