# Lab7.py
# Name 1: Thomas Marshall
# Name 2: N/A

def numberWords():
    rawWords = open("rawWords.txt", "r")
    numberWords = open("numberWords.txt", "w")

    full = []
    for line in rawWords:
        words = line.split()
        full += words

    for i in range(len(full)):
        print(str(i + 1) + ". " + full[i], file = numberWords)
        

    rawWords.close()

def hourlyWages(infileName, outfileName):
    iniWage = open(infileName, "r")
    newWage = open(outfileName, "w")

    for line in iniWage:
        wageList = line.split()
        raises = str("{0:.2f}".format(eval(wageList[2]) + 1.65))
        print(wageList[0] + " " + wageList[1] + " $" + raises + " " + wageList[3],
              file = newWage)

def thirds():
    sentNum = eval(input("Input how many sentences will be entered: "))

    for i in range(sentNum):
        sent = input("\nEnter sentence " + str(i + 1) + ": ")
        sent = sent.strip()
        for j in range(2, len(sent) + 1, 3):
            print(sent[j], end = "")

    print("")

def wordCount(sentence):
    sentenceList = sentence.split()
    word = len(sentenceList)
    return word

def characterCount(sentence):
    wordList = sentence.replace(" ","")
    characterList = []
    for character in wordList:
        letter = character
        characterList += [letter]
        
    character = len(characterList)
    return character
    
def wordAverage():
    sentCount = eval(input("Enter the number of sentences: "))
    for i in range(sentCount):
        sent = input("Enter sentence " + str(i + 1) + ": ")
        words = wordCount(sent)
        characters = characterCount(sent)
        characterAvg = characters / words
        print("\nAverage number of characters per word in sentence " + str(i + 1) + ": " + 
              str(characterAvg) + ".\n")

#main() should be the only file executed when you are checked off for this lab
#thus add code to main() to call any functions you write.
def main():
    numberWords()
    hourlyWages("hourlyWages.txt", "newWage.txt")
    thirds()
    print(wordCount("The quick brown fox jumps over the lazy dog"))
    print(characterCount("Isn't lab fun!"))
    wordAverage()
main()
