import random
import setup
level = 0
level = setup.setup(level)
if level == 4:
  insane=open('insane.txt', 'r')
  word_bank = insane.read()
  word_bank = word_bank.split(', ')
else:
  hangman=open('hangman.txt', 'r')
  word_bank = hangman.read()
  word_bank = word_bank.split(', ')
letters_guessed = []
answer = []
wrong_guesses = []
hangman =  ['''
    ______
    |     |
    |     
    |    
    |    
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    
    |   
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |     |
    |    
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|
    |    
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|\\
    |    
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|\\
    |    / 
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|\\
    |    / \\
    ---------
    |       |
    ---------''']
lives = 0
word = random.choice(word_bank)
word_to_guess=[]
#initializes word_to_guess
while True:
  for i in range(len(word)):
    word_to_guess.append(word[i])   
  if level == 4:
    break
  elif len(word_to_guess) < 6 and level == 0:
    break
  elif len(word_to_guess)>5 and len(word)<7 and level == 1:
    break
  elif len(word_to_guess)>7 and len(word)<10 and level == 2:
    break
  elif len(word_to_guess)>10 and level == 3:
    break
  else:
      word = random.choice(word_bank)
  word_to_guess=[]
#sets up answer based on word length
for i in range(len(word_to_guess)):
  if word_to_guess[i] == ' ':
    answer.append(' ')
  elif word_to_guess[i] == '-':
    answer.append('-')
  else:
    answer.append('_')
running=True
you_won='''  ⁔ ⁔ ⁔ ⁔ ⁔ ⁔ ⁔ ⁔
 (   YOU WON!    )
  ⁀ ⁀ ⁀ ⁀ ⁀ ⁀ ⁀ ⁀'''
you_lost='''  ___________
  | You Lost |
  ‾‾‾‾‾‾‾‾‾‾‾'''