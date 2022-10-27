import random

#MUST be a 4 letter word 
word_bank = [['v','e','r','y'],['k','i','n','k']]
words_guessed = []
answer = ['_','_','_','_']
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
    |    /|\
    |    
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|\
    |    / 
    ---------
    |       |
    ---------''','''
    ______
    |     |
    |     O
    |    /|\
    |    / \
    ---------
    |       |
    ---------''']
lives = 0
word_to_guess = random.choice(word_bank)
place_holder = "_ "
while True:

  
  print(hangman[lives])
  for i in range(len(words_guessed)):
    rnd = i
    for j in range(len(word_to_guess)):
      stop=False
      if words_guessed[rnd] == word_to_guess[j]:
        answer[j]=words_guessed[rnd]
        stop = True
      elif words_guessed[rnd] not in wrong_guesses and not stop:
        lives+=1
        print('    INCORRECT')
        wrong_guesses.append(words_guessed[rnd])
  print("    ",end = "",)
  for i in range(4):
    print(answer[i],end = "")
    print(" ",end = "")
  print('\n   ',wrong_guesses)
  Input = input('\n\nGuess a letter:\n>>> ')
  words_guessed.append(Input)
  print('\n'*7)