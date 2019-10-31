## Thomas Marshall
## lab3.py

from graphics import *
from math import *
# Create a blue circle on a yellow background
def makeCircle():
    # dimensions for the window
    width = 400
    height = 500
    win = GraphWin("Blue Circle on Yellow", width, height)
    win.setBackground("yellow")
    # create the circle
    centerPoint = Point(width/2, height/2)
    circle = Circle(centerPoint, 50)
    circle.setFill("blue")
    # place the circle in the window
    circle.draw(win)
    
#Complete
# Calculate the average of a group of numbers per assignment instructions
def average():
    print("Finds average")
    #Definitions
    hw = eval(input("Enter how many homework grades you have: "))
    total = 0
    print()
    #Range to calculate average grades
    for i in range(hw):
        grade = eval(input("Enter your grade on HW" + str(i+1) + ": "))
        total = total + grade
    avg = total/hw
    #Gives average
    print("\nAverage:", avg)

#Complete
# Approximates the square root of a number using Sir Isaac Newton's method
def newton():
    #Definitions
    x = eval(input("Enter the value of x: "))
    improve = eval(input("\nHow many times should the approximation be improved? "))
    approx = x/2

    #Range to calculate the square root
    for i in range(improve):
        approx = (approx + (x/approx))/2

    #Gives final answer
    print("\nFinal value:", approx)

#Complete
# Builds a white house with a brown roof on a blue background
def buildHouse():
    # dimensions for the window
    width = 400
    height = 500
    win = GraphWin("House with a blue background", width, height)
    win.setBackground("blue")
    # create the house
    sPt1 = Point(100, 150)
    sPt2 = Point(300, 350)
    square = Rectangle(sPt1, sPt2)
    square.setFill("white")
    # place the house in the window
    square.draw(win)

    # create roof
    tPt1 = Point(300, 150)
    tPt2 = Point(200, 50)
    tri = Polygon(sPt1, tPt1, tPt2)
    tri.setFill("brown")
    # place the roof in the window
    tri.draw(win)

#Complete
#Creates a rectangle and gives perimeter and area
def rectangle():
    # dimensions for the window
    width = 600
    height = 600
    win = GraphWin("Build a rectangle", width, height)
    win.setBackground("blue")

    #Written instructions
    instructions = Text(Point(width/2, height - 90), "")
    instructions.setText("Click two points you want to be opposite points of a rectangle.")
    instructions.draw(win)

    # Create the rectangle
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    rect = Rectangle(pt1, pt2)
    rect.setFill("green")
    # Place the rectangle in the window
    rect.draw(win)

    #Gives area and perimeter
    length = abs(pt2.getX() - pt1.getX())
    wide = abs(pt2.getY() - pt1.getY())
    perimeter = 2 * length + 2 * wide
    peri = Text(Point(width/2, height - 60), "")
    peri.setText("The perimeter of the rectangle is " + str(perimeter) + ".\n")
    peri.draw(win)
    area = length * wide
    a = Text(Point(width/2, height - 30), "")
    a.setText("The area of the rectangle is " + str(area) + ".")
    a.draw(win)
    
    # Closes window
    clickPt = win.getMouse()
    win.close()

# Complete
# Lets the user create a circle
def circle():
    # dimensions for the window
    width = 600
    height = 600
    win = GraphWin("Blue Circle on Yellow", width, height)
    win.setBackground("blue")
    # create the circle
    centerPoint = win.getMouse()
    circumference = win.getMouse()
    radius = abs(sqrt((circumference.getX() - centerPoint.getX())**2 + (circumference.getY() - centerPoint.getY())**2))
    circle = Circle(centerPoint, radius)
    circle.setFill("red")
    # place the circle in the window
    circle.draw(win)

    # Closes window
    instructions = Text(Point(width/2, height - 30), "")
    instructions.setText("Please, click to close.")
    instructions.draw(win)
    clickPt = win.getMouse()
    win.close()

#Lets the user create a sequence
def sequence():
    terms = eval(input("Enter the number of terms: "))
    total = 0
    for i in range(1,terms+1,terms):
        total = 2*i + total
        print(total)
        
        
    
        
def main():
    makeCircle()
    average()
    newton()
    buildHouse()
    rectangle()
    circle()
    #sequence
