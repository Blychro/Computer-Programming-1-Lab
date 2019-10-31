# Lab5.py
# Name 1: Sam
# Name 2: Thomas

from graphics import *
from math import *

def target():
    winWidth = 100
    winHeight = winWidth
    win = GraphWin("Archery Target", winWidth, winHeight)
    center=Point(winWidth/2,winHeight/2)
    width=winWidth*(2/5)
    # Add code here to get the dimensions and draw the target
    white=Circle(center,width)
    black=Circle(center,width*(4/5))
    blue=Circle(center,width*(3/5))
    red=Circle(center,width*(2/5))
    yellow=Circle(center,width/5)
    white.setFill("white")
    white.draw(win)
    black.setFill("black")
    black.draw(win)
    blue.setFill("blue")
    blue.draw(win)
    red.setFill("red")
    red.draw(win)
    yellow.setFill("yellow")
    yellow.draw(win)
    # Wait for another click to exit
    message=Text(Point(winWidth/2,winHeight-20),"Click anywhere to close")
    message.draw(win)
    win.getMouse()
    win.close()



def triangle():
    winWidth = 500
    winHeight = 500
    win = GraphWin("Draw a Triangle", winWidth, winHeight)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()

    tri = Polygon(p1, p2, p3)
    tri.setFill("blue")
    tri.draw(win)

    side1 = sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    side2 = sqrt((p3.getX() - p2.getX())**2 + (p3.getY() - p2.getY())**2)
    side3 = sqrt((p1.getX() - p3.getX())**2 + (p1.getY() - p3.getY())**2)
    perimeter = side1 + side2 + side3
    s = (side1 + side2 + side3)/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    # and display its area in the graphics window.
    message1 = Text(Point(winWidth/2, winHeight - 30), "Area="+str(area))
    message2 = Text(Point(winWidth/2, winHeight - 15), "Perimeter="+str(perimeter))
    message1.draw(win)
    message2.draw(win)
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

def processString():
    phrase=str(input("Please enter a string: "))
    print(phrase[0])
    print(phrase[len(phrase)-1])
    print(phrase[2:6])
    print(phrase[0]+phrase[len(phrase)-1])
    for i in range(10):
        print(phrase[0:3])
    for i in range(len(phrase)):
        print(phrase[i])
    print(len(phrase))

def processList():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1]+values[3]
    print(x)
    x = values[0]+values[2]
    print(x)
    x = values[1]*5
    print(x)
    x = [values[2],values[3],values[4]]
    print(x)
    x = [values[2],values[3],values[0]]
    print(x)
    x = [values[2],values[0],float(values[5])]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = len(values)
    print(x)
    
def colorShape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    #create window
    winWidth = 400
    winHeight = 400
    win = GraphWin("Color Shape", winWidth, winHeight)
    win.setBackground("white")

    #create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(winWidth/2, winHeight-20), msg)
    inst.draw(win)

    #create circle in window's center
    shape = Circle(Point(winWidth/2, winHeight/2 - 30), 50)
    shape.draw(win)

    #redTexPt is 50 pixels to the left and forty pixels down from center
    redTextPt = Point(winWidth/2 - 50, winHeight/2 + 40)
    redText = Text(redTextPt, "Red: ")
    redText.setTextColor("red")
    redEntry=Entry(Point(winWidth/2,winHeight/2+40),5)

    #greenTextPt is 30 pixels down from red
    greenTextPt = redTextPt.clone()
    greenTextPt.move(0,30)
    greenText = Text(greenTextPt, "Green: ")
    greenText.setTextColor("green")
    greenEntry=Entry(Point(winWidth/2+5,winHeight/2+70),5)

    #blueTextPt is 60 pixels down from red
    blueTextPt = redTextPt.clone()
    blueTextPt.move(0,60)
    blueText = Text(blueTextPt, "Blue: ")
    blueText.setTextColor("blue")
    blueEntry=Entry(Point(winWidth/2,winHeight/2+100),5)

    #display rgb text
    redText.draw(win)
    redEntry.draw(win)
    greenText.draw(win)
    greenEntry.draw(win)
    blueText.draw(win)
    blueEntry.draw(win)
    for i in range(5):
        win.getMouse()
        shape.setFill(color_rgb(int(redEntry.getText()),int(greenEntry.getText()),
                                int(blueEntry.getText())))
    win.getMouse()
    win.close()

def anotherSeries():
    n = int(input("Enter n number of terms: "))
    total=0
    temp=0
    for i in range(n):
        temp=temp%6
        temp+=2
        total+=temp
        print(str(temp)+" + ",end=" ")
    print()
    print(total)

def anotherSeriesPartner():
    n = int(input("Enter n number of terms: "))
    num = 1
    den = 3
    total=1
    for i in range(n):
        total *= (num/den)
        print(str(num)+"/"+str(den)+" * ",end="")
        num += 2
        den *= 2
    print("\n", total)
    
def main():
    target()
    triangle()
    processString()
    processList()
    colorShape()
    anotherSeries()
    anotherSeriesPartner()

main()





