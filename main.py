import settings, os, playsound
#playsound.playsound('storm.mp3', False)
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
    if settings.letters_guessed[rnd] not in settings.answer and settings.letters_guessed[rnd] != '':
      settings.lives+=1
      if settings.lives!= 7:
        print("\033[31m",'    INCORRECT',"\033[0m")
      settings.wrong_guesses.append(settings.letters_guessed[rnd]) 
      settings.letters_guessed.pop(rnd)

  #checks if you lost
  if settings.lives==7:
    print(settings.you_lost)
    print('Answer is:',settings.word)
    print('\n'*3)
    settings.running=False
    
  #prints gallows
  if settings.running:
    print(settings.hangman[settings.lives])
    print("    ",end = "",)
    
    #prints lines under gallows
    for i in range(len(settings.answer)):
      print(settings.answer[i],end = "")
      print(" ",end = "")
      
    #prints wrong guesses
    print('\n   ',end = "")
    print('[',end = "")
    for i in range(len(settings.wrong_guesses)):
      print("\033[31m",settings.wrong_guesses[i],"\033[0m",end = "")
    print(']')
    Input = input('\n\nGuess a letter:  \n(if there are no more slots to fill, press enter)\n>>> ')
    settings.letters_guessed.append(Input)
    os.system('clear')
    
    #checks if you won
    if settings.answer==settings.word_to_guess:
      print(settings.you_won)
      print('\n'*3)
      settings.running=False
