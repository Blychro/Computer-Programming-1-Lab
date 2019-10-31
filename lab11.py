# Thomas Marshall
# hangman.py

import random

def secretList():
    words = open("wordlist.txt", "r")
    wordList = []
    for word in words:
        word = word.replace("\n", "")
        wordList.append(word)
    randWord = random.randrange(0, len(wordList)-1)
    word = wordList[randWord]
    return word

def wordFind(word):
    letters = []
    for letter in word:
        letters += letter
    return letters

def gameWord(word):
    show = []
    for i in range(len(word)):
        show += "_"
    return show

def replace(word, newWord, guess):
    count = 0
    count2 = 0
    turn = False
    for letter in word:
        if letter == guess:
            newWord[count] = letter
        else:
            count2 += 1
        count += 1
    if count != count2:
        turn = True
    return turn

def guess(word, newWord):
    miss = 1
    lives = str(8 - miss)
    print("Lives = " + lives)
    print(newWord)
    
    while miss <= 7 and newWord != word:
        letterGuess = input("\nEnter a letter: ")
        print("\n---------------------------------------------------\n")
        replace(word, newWord, letterGuess)
        if replace(word, newWord, letterGuess) != True:
            miss += 1
            lives = str(8 - miss)
        print("Lives = " + lives)
        print(newWord)
        
    if newWord == word:
        print("\nYou Win!")
    else:
        print("\nYou Lose! :(")

def letters():
    word = secretList()
    wordSelect = wordFind(word)
    newWord = gameWord(word)
    guess(wordSelect, newWord)

letters()
