import random

def introToHangman(name):
    print('Hi ' + name + ', welcome to Hangman')

def getGuess(alreadyGuessedLetters):
    while True:
        print('Guess the letter')
        guess = input().lower()
        
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessedLetters :
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyzöäü':
            print('Special characters and numbers are not allowed. Choose again.')
        else:
            return guess

def getRandomWord(words):
    wordIndex = random.randint(0, len(words)- 1)
    return words[wordIndex]

def printHangmanPic(hangmanIndex, hangmanPic) :
        print(hangmanPic[hangmanIndex])
        print()

def checkTheLetter(secretWord, guessedLetter) :
    if guessedLetter in secretWord : 
        return True
    return False

def showBoard(hangmanPic, missedLetters, correctGuessedLetters, secretWord) :
    printHangmanPic(len(missedLetters), hangmanPic)
    print()
    
    print('Missed letters :', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    # replace blank with the correct guessed letter
    for i in range(len(secretWord)) :
        if(secretWord[i] in correctGuessedLetters):
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            # blanks[i] = secretWord[i]

    for letter in blanks :
        print(letter, end = ' ')
    print()

    if(blanks == secretWord or len(missedLetters) >= 6):
        if(blanks == secretWord):
            print('You win !!')
        elif(len(missedLetters) >= 6):
            print('Oh you lost, the word you were gussing was ' + secretWord)
        return True
    return False

HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
/    |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
 =========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
 =========''']

words = 'schlafen sprechen reden teilnehmer'.split()
#missedLetters = 'no letters are missed'
#correctGuessedLetters = 'no correct words are been set'

print('Please enter your name')
name = input()
playAgain ='yes'
while playAgain == 'yes' or playAgain == 'y' :
    missedLetters = ''
    correctGuessedLetters = ''
    secretWord = getRandomWord(words)
    endOfGame = False
    while not(endOfGame):
        introToHangman(name)
        endOfGame = showBoard(HANGMANPICS, missedLetters, correctGuessedLetters, secretWord)
        if not(endOfGame):
            guess = getGuess(correctGuessedLetters+missedLetters)

            if checkTheLetter(secretWord, guess):
                correctGuessedLetters = correctGuessedLetters + guess
            else :
                missedLetters = missedLetters + guess
           
    print('Would like to play again (y/n)?')
    playAgain = input()
