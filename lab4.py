## Thomas Marshall
## lab4.py

from graphics import *

# Completed
def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    #Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    #number of times user can move circle
    numClicks = 6

    #create a space to instruct user
    instPt = Point(width/2, height-10)
    instructions = Text(instPt,"Click to move squares")
    instructions.draw(win)

    #builds a circle
    center = win.getMouse()
    pt1 = Point(center.getX() - 20, center.getY() - 20)
    pt2 = Point(center.getX() + 20, center.getY() + 20)
    shape = Rectangle(pt1, pt2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    #allows the user to click multiple times to move the
    #circle
    for i in range(numClicks):
        p = win.getMouse()

        #move amount is distance from center of circle to the
        #point where the user clicked
        nPt1 = Point(p.getX() - 20, p.getY() - 20)
        nPt2 = Point(p.getX() + 20, p.getY() + 20)
        nShape = Rectangle(nPt1, nPt2)
        nShape.setOutline("red")
        nShape.setFill("red")
        nShape.draw(win)
        
        

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

#Completed
def cupConverter():
    # Author: RoxAnn H. Stalvey, modified by Walter Pharr
    # Illustrates getting numeric input through graphics window
    winWidth = 300
    winHeight = 200
    win = GraphWin("Convert cups to milliliters", winWidth, winHeight)

    #Specify the message for the input box
    boxDesc = Text(Point(100, 50), "Input cups: ")
    boxDesc.draw(win)

    #Create the Entry object and set its default text to a number
    #  allowing the user to see what type of value is expected
    inp = Entry(Point(200, 50), 5)
    inp.setText("")
    inp.draw(win)

    #Create a Text object for outputting the result
    output = Text(Point(150, 150), "")
    output.draw(win)

    #This button isn't necessary, but it makes a nice point for the user
    #  to click.  If you click anywhere in the window, the code reacts
    #  the same way.
    btPtX = winWidth/2
    btPtY = winHeight/2
    button = Text(Point(btPtX, btPtY), "Click")
    button.draw(win)
    border = Rectangle(Point(btPtX-35, btPtY-20), Point(btPtX+35, btPtY+20))
    border.draw(win)

    # Wait for a mouse click
    win.getMouse()

    # Discover intput and convert it to a number
    # If numeric input wasn't needed, simply omit the eval()
    cups = eval(inp.getText())
    oz = cups * 8
    mL = oz * 29.57
    #Calculate milliliter equivalent here

    # Display output and change button
    output.setText("Milliliters = " + str(mL))
    button.setText("Quit")
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

# Completed
# Creates a sequence
def sequence():
    # Input for terms
    terms = eval(input("Enter the number of terms: "))
    # Range to create sequence
    for i in range(terms):
        print(i + i%2 + 1, end=" ")

# Completed
def pi():
    n = eval(input("Enter  n: "))
    pi = 1
    for i in range(n):
        numerator = i + 1 + (i+1)%2
        denominator = i + i%2 + 1
        pi = pi * numerator / denominator
    print(pi*2)

# Completed
def fibonacci():
    num1 = 0
    num2 = 1
    terms = eval(input("Enter the number of terms: "))
    for i in range(terms):
        temp = num2
        num2 = num1 + num2
        num1 = temp
        print(num1)

# Completed
def pi2():
    pi = 0
    start = 0-1
    terms = eval(input("Enter the number of terms: "))
    for i in range(terms):
        start = start + 2
        pi = pi + (4/start) * (0-1)**(i)
    print(pi)
        
def main():
    squares()
    cupConverter()
    sequence()
    fibonacci()
    pi()
    pi2()
 
main()
