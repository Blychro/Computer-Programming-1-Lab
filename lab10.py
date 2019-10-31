# CSCI 220L - Lab 10
#
# Name 1:
#
# Name 2:
#

from graphics import *
from random import randint
from time import sleep

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
    while True:
        centerPoint = circle.getCenter()
        newX = randint(-centerPoint.getX(), width - centerPoint.getX())
        newY = randint(-centerPoint.getY(), height - centerPoint.getY())
        circle.move(newX, newY)
        sleep(.1)


    
    
    
