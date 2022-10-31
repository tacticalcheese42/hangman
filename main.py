import settings

while settings.running:

  #begins checks
  for i in range(len(settings.letters_guessed)):
    
    rnd = i
    for j in range(len(settings.word_to_guess)):
      
      stop=False
      #checks if guess was correct
      if settings.letters_guessed[rnd] == settings.word_to_guess[j]:
        settings.answer[j]=settings.letters_guessed[rnd]
     #checks if guess was incorrect 
    if settings.letters_guessed[rnd] not in settings.answer:
      settings.lives+=1
      if settings.lives!= 7:
        print('    INCORRECT')
      settings.wrong_guesses.append(settings.letters_guessed[rnd]) 
      settings.letters_guessed.pop(rnd)

  #checks if you lost
  if settings.lives==7:
    print(settings.you_lost)
    print('Answer is:',settings.word)
    print('\n'*3)
    settings.running=False
    
  #prints gallows
  if settings.lives !=7:
    print(settings.hangman[settings.lives])
  
    print("    ",end = "",)
    #prints lines under gallows
    for i in range(len(settings.answer)):
    
      print(settings.answer[i],end = "")
      print(" ",end = "")
    
    print('\n   ',settings.wrong_guesses)
    Input = input('\n\nGuess a letter:  \n(if there are no more slots to fill, press enter)\n>>> ')
    settings.letters_guessed.append(Input)
    print('\n'*15)
    #checks if you won
    if settings.answer==settings.word_to_guess:
      print(settings.you_won)
      print('\n'*3)
      settings.running=False
