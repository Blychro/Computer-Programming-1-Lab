# Lab6.py
# Name 1: Hollande Powell
# Name 2: Thomas Marshall

def functionPractice():
    print("It's raining {1} and {0}.".format("dogs","cats"))
    print("{0:.2f} {1:.3f}".format(2.3,.4567))
    print("Time left 0{0}:0{1:2.2f}".format(3, 7.4589))
    print("{0} {1}: {2:.2f}".format("Steph", "Curry", 43.75432))

def nameReverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("What is your name? ")
    splitName = name.split()
    first= splitName[0]
    last = splitName[1]
    print("Your name is {1}, {0}".format(first, last))

def companyName():
    site = input("Enter a website address: ")
    siteList = site.split(".")
    print(siteList[1])

def encode():
    word = input("Enter a word: ")
    key = eval(input("Enter the key: "))
    word = word.lower()
    newWord = ""
    for ch in word:
        letter = chr(ord(ch) + key)
        newWord += letter
    print(newWord)

def encodeBetter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    word = input("Enter a word: ")
    key = eval(input("Enter the key: "))

    word = word.lower()
    newWord = ""

    for ch in word:
        letter = alphabet[((ord(ch)-ord("a") + key)%26)]
        newWord += letter
    print(newWord)
    
def initials():
    num = eval(input("Enter the number of students: "))
    for i in range(num):
        first = input("Enter the first name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        print(first + "'s initials are " + first[0] + last[0] + ".")

def names():
    names = input("Enter a list of names, separated by commas: ")

    nameList = names.split(",")
    initials = ""
    initialList = ""
    for name in nameList:
        name = name.split()
        first = name[0]
        firstInitial = first[0]

        last = name[1]
        lastInitial = last[0]

        initials = firstInitial + lastInitial + " "
        initials = initials.upper()
        initialList += initials
    initialList = initialList.strip()
    
    print("The initials are " + initialList)
    
def main():
    nameReverse()
    functionPractice()
    companyName()
    encode()
    encodeBetter()
    initials()
    names()
main()
