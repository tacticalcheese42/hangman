import random
import setup
level=0
level=setup.setup(level)
hangman=open('hangman.txt', 'r')
#MUST be a 4 letter word 
word_bank = hangman.read()
word_bank = word_bank.split(', ')
#what letters you've guessed
letters_guessed = []
#display of answer thus far
answer = []
#what  you've guessed wrong
wrong_guesses = []
#what hangman looks like
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
#how many lives you've used
lives = 0
#which word you have to guess
word = random.choice(word_bank)
word_to_guess=[]
#initializes word_to_guess
while True:
  for i in range(len(word)):
    word_to_guess.append(word[i])
    
  if len(word_to_guess) < 6 and level == 0:
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
  answer.append('_')
#if you haven't won yet 
running=True
#you won message
you_won='''  ⁔ ⁔ ⁔ ⁔ ⁔ ⁔ ⁔ ⁔
 (   YOU WON!    )
  ⁀ ⁀ ⁀ ⁀ ⁀ ⁀ ⁀ ⁀'''
you_lost='''  ___________
  | You Lost |
  ‾‾‾‾‾‾‾‾‾‾‾'''