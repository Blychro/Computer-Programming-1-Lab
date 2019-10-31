# name 1 - Thomas Marshall
# name 2 - Kasper Dugaw
# name 3 - Clare Cleaver

from point import Point
import math

class Circle:
    def __init__(self,xVal,yVal,radius):
        self.center = Point()
        self.center.setX(xVal)
        self.center.setY(yVal)
        self.radius = radius

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def setCenter(self,centerX, centerY):
        self.center.setX(centerX)
        self.center.setY(centerY)
        

    def setRadius(self,radius):
        self.radius = radius

    def area(self):
        radius = self.radius
        circArea = math.pi * radius ** 2
        return circArea

    def __str__(self):
        value = ("Circle:\n\tCenter: "+str(self.getCenter())+"\n\tRadius: "+
                 str(self.getRadius())+"\n\tArea: "+str(self.area()))
        return value
        
