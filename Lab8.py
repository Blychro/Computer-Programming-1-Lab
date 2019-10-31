## Lab9.py
##
## Name 1: Wes Ford
##
## Name 2: Thomas Marshall
##

from graphics import *
from math import sqrt

def squareEach(numList):
    for i in range(len(numList)):
        numList[i] **= 2
    
def sumList(numList):
    total = 0
    for num in numList:
        total += num
    return total

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    

def sumOfSquares(numList):
    toNumbers(numList)
    squareEach(numList)
    total = sumList(numList)
    print(total)

def calcDistance(point1, point2):
    """
    Calculates the distance between two points.
    """
    x1, y1 = point1.getX(), point1.getY()
    x2, y2 = point2.getX(), point2.getY()
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
def starter():
    """
    Ask for a wrestler's weight and number of wins, determine whether
    the wrestler is a starter.
    """
    weight = float(input("Enter your weight: "))
    numWins = int(input("Enter your number of wins: "))
    if weight >= 150 and weight < 160 and numWins >= 5:
        print("You should start on the wrestling team.")
    else:
        if weight > 199 or numWins > 20:
            print("You should start on the wrestling team.")
        else:
            print("You should not start on the wrestling team.")

def isValid(isbn):
    position = len(isbn)
    total = 0
    for i in range(len(isbn)):
        total += int(isbn[i]) * position
        position = position - 1
    return total % (len(isbn) + 1) == 0
        
def circleOverlap():
    """
    Draw two circles and determine whether they overlap.
    """
    #Build window
    winHeight = 400
    winWidth = 400
    win = GraphWin("Overlapping circles", winHeight, winWidth)

    #Text area for instructions for user
    instruct = Text(Point(winWidth/2, winHeight-10), "")
    instruct.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a circle, click the centerpoint for the circle")
    center = win.getMouse()
    center.draw(win)

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the circle.")
    border = win.getMouse()

    #Calculate radius using Euclidean distance
    radius = calcDistance(center, border)
    circle = Circle(center, radius)
    circle.draw(win)

    #Get center point and x/y for center
    instruct.setText("To draw a second circle, click the centerpoint for the circle")
    center2 = win.getMouse()
    center2.draw(win)

    #Get point on the circumference and its x/y coordinates
    instruct.setText("Click a point on the border of the second circle.")
    border2 = win.getMouse()

    #Calculate radius using Euclidean distance
    radius2 = calcDistance(center2, border2)
    circle2 = Circle(center2, radius2)
    circle2.draw(win)

    radiusSum = radius + radius2

    if calcDistance(center, center2) <= radiusSum:
        instruct.setText("The circles overlap. Click anywhere to close.")
    else:
        instruct.setText("The circles don't overlap. Click anywhere to close.")

    # Wait for another click to exit
    win.getMouse()
    win.close()

def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        if year % 400 == 0:
            return True
        else:
            return False
        return False
            

def main():
    ''' Add code to test all of your functions '''
    #sumOfSquares(["3", "5.7", "2"])
    #starter()
    #boolean = isValid("00729465201")
    #print(boolean)
    #circleOverlap()
    year = 2005
    isLeap = leapYear(year)
    if isLeap == True:
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year.")
main()
