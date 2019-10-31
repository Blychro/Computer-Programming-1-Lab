# CSCI 220L - Lab 10
#
# Name 1: Thomas Marshall
#
# Name 2: Nick Mancabelli
#

from graphics import *
from random import randint
from time import sleep

# Reason to stop: when float is added int times
# Reason to loop: when float is added less than in times
def calculateSum(value, numIterations):
    numFloat = value
    count = 1
    while count < numIterations:
        value += numFloat
        count += 1
    return value

def areEqual(num1, num2):
    return abs(num1 - num2) <= .0001

#Reason to stop: When user enters correct input
#Reason for loop: When the input is incorrect
def goodInput():
    num = eval(input("Enter a number 1 through 10, -1, or greater than 50: "))
    while (num < 1 or num > 10) and num != -1 and num <= 50:
        print("Please try again, read the instructions moron.")
        num = eval(input("Enter a number 1 through 10, -1, or greater than 50: "))
    print(num)

# Reason to stop: When the number is less than 1
# Reason to loop: When the number is not less than 1
def numDigits():
    num = float(input("Enter a positive number: "))
    while num >= 1:
        count = 0
        while num >= 1:
            num /= 10
            count += 1
        print(count)
        num = eval(input("Enter a positive number: "))

#Reason to stop: When the user guesses the correct number
#Reason to loop: Continue the game 
def hiLoGame():
    count = 1
    num = randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    while count < 7 and guess != num:
        if guess < num:
            print("Too Low")
        else:
            if guess > num:
                print("Too High")
            else:
                if guess == num:
                    print("Correct!")
        count += 1
        guess = int(input("Guess a number between 1 and 100: "))

    if count < 7 or num == guess:
        print("You win in " + str(count) + " guesses!")
    else:
        print("Sorry you lose, the number was:", num)

def isClicked(rectangle, click):
    rectP1 = rectangle.getP1()
    rectP1X = rectP1.getX()
    rectP1Y = rectP1.getY()
    rectP2 = rectangle.getP2()
    rectP2X = rectP2.getX()
    rectP2Y = rectP2.getY()
    clickX = click.getX()
    clickY = click.getY()
    return clickX >= rectP1X and clickY >= rectP1Y and clickX <= rectP2X and clickY <= rectP2Y
                
    
# Reason to stop: when mouse is clicked inside the rectangle
# Reason to loop: when mouse is not clicked inside the rectangle
def randomCircle():
    # define the dimensions of the display
    height = 400
    width = 500
    win = GraphWin("Random Circle", width, height)
    # create the initial circle
    radius = 10
    cX = randint(radius, width - radius)
    cY = randint(radius, height - radius)
    centerPoint = Point(cX, cY)
    circle = Circle(centerPoint, radius)
    circle.setFill("blue")
    circle.draw(win)
    # create the red rectangle
    topLeft = Point(width - 60, height - 40)
    bottomRight = Point(width, height)
    rect = Rectangle(topLeft, bottomRight)
    rect.setFill("red")
    rect.draw(win)

    # loop that moves the circle randomly
    stop = False
    while stop != True:
        centerPoint = circle.getCenter()
        newX = randint(-centerPoint.getX(), width - centerPoint.getX())
        newY = randint(-centerPoint.getY(), height - centerPoint.getY())
        circle.move(newX, newY)
        sleep(.1)
        click = win.checkMouse()
        if click != None:
            stop = isClicked(rect, click)


def main():
##    result = calculateSum(.1, 10)
##    equals = areEqual(1.0, result)
##    if equals == True:
##        print("The two numbers are equal.")
##    else:
##        print("The two numbers are not equal.")
##    
##    goodInput()
##    numDigits()
##    hiLoGame()
    
    randomCircle()
main()
    
    
