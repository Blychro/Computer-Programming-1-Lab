# name 1 - Thomas Marshall
# name 2 - Kasper Dugaw
# name 3 - Clare Cleaver

class Point:
    def __init__(self):
        self.xVal = 0
        self.yVal = 0

    def getX(self):
        return self.xVal

    def getY(self):
        return self.yVal

    def setX(self, xVal):
        self.xVal = xVal

    def setY(self, yVal):
        self.yVal = yVal
    
    def __str__(self):
        point = "("+str(self.getX())+", "+str(self.getY())+")"
        return point
