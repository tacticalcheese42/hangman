import random

#MUST be a 4 letter word 
word_bank = [['v','e','r','y'],['k','i','n','k']]
words_guessed = ['e','v','k','n']
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
print(hangman[lives])
place_holder = "_ "
for i in range(len(words_guessed)):
  rnd = i
  for j in range(len(word_to_guess)):
    if words_guessed[rnd] == word_to_guess[j]:
      print(words_guessed[rnd])
print("    ",end = "",)
for i in range(4):
  print(place_holder,end = "",)
