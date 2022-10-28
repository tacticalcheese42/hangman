import settings

while settings.running:

  
  print(settings.hangman[settings.lives])
  for i in range(len(settings.words_guessed)):
    
    rnd = i
    for j in range(len(settings.word_to_guess)):
      
      stop=False
      if settings.words_guessed[rnd] == settings.word_to_guess[j]:
        settings.answer[j]=settings.words_guessed[rnd]
     #PROBLEMS   
    if settings.words_guessed[rnd] not in settings.answer:
      settings.lives+=1
      print('    INCORRECT')
      settings.wrong_guesses.append(settings.words_guessed[rnd]) 
      
  print("    ",end = "",)
  for i in range(4):
    
    print(settings.answer[i],end = "")
    print(" ",end = "")
    
  print('\n   ',settings.wrong_guesses)
  Input = input('\n\nGuess a letter:  \n(if there are no more slots to fill, press enter)\n>>> ')
  settings.words_guessed.append(Input)
  print('\n'*7)
  if settings.answer==settings.word_to_guess:
    print('''YOU WON!''')
    settings.running=False
