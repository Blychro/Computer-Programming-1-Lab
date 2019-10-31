##name1: Thomas Marshall
##name2: Swapnil Srivastava



##observations for sortTest
##the selection sort took 2.80827 seconds
##the python's selection takes 0.0 seconds, hence python's selection is more efficient

##observations for searchTest:
##    for 14 elements, both linear and binary take roughly the same amount of time, because the list is small it takes virtually no time.
##
##    for the List with 10000950 elements, linear takes less time if the element is present in the list, but binary takes less time if the element is not in the list.
##    This is because binary has to take less steps to check for the existence of the element.
    
from time import sleep
from graphics import *
from random import shuffle


# draws a list of rectangles one a time while waiting one second in between
# rectangle so you can actually see them being draw in order
def drawRectangleList(rectList, win):
    for rect in rectList:
        rect.draw(win)
        time.sleep(1)

def reverseSort(list1):
    list1.sort()
    list1.reverse()
    print(list1)

def findAndRemoveFirst(mylist, value):
    pos = mylist.index(value)
    mylist.insert(pos, "thomas")
    mylist.remove(value)
    print(mylist)
            
def findAndPopFirst(mylist, value):
    pos = mylist.index(value)
    popit = mylist.pop(pos)
    mylist.insert(pos, "thomas")
    print(mylist)

def readData(filename):
    numList = []
    for num in filename:
        string = num.split()
        numList += string
##    for num in numList:
##        num = int(num)
    return numList

def isInLinear(searchVal, values):
    search = False
    count = 0
    while search == False and count < len(values):
        if values[count] == searchVal:
            search = True
        count += 1
    return search

def isInBinary(searchVal, values):
    search = False
    values.sort()
    high = len(values) - 1
    low = 0
    mid = (high - low)//2
    
    count= 0
    while mid != searchVal and count<len(values):
        if searchVal< mid:
            high = mid-1
        elif searchVal>mid:
            low = mid+1
        mid = (high - low)//2
        count += 1
    if mid == searchVal:
        search = True
    return search

def selSort(values):
    for i in range(len(values) - 1):
        count = i
        for j in range(count + 1, len(values)):
            if values[j] < values[count]:
                count = j

        temp = values[count]
        values[count] = values[i]
        values[i] = temp
    return values

                     
    
# creates a list of 10 rectangles that are drawn within each other; when the
# list is sorted and drawn correctly you should be able to see all rectangles
def populateRectangleList(rectList, win):
    height = win.getHeight()
    width = win.getWidth()
    numberOfRectangles = 10
    denom = numberOfRectangles * 2
    colors = ["red", "white"]
    for i in range(numberOfRectangles):
        p1 = Point(width * i/denom, height * i/denom)
        p2 = Point(width * (denom - i)/denom, height * (denom - i)/denom)
        temp = Rectangle(p1, p2)
        temp.setFill(colors[i % 2])
        rectList.append(temp)
    # comment out this line below to see what your display should look like
    # after you are completed with your sort;
    # DO NOT COMMENT THIS LINE AND TRY TO TURN IT IN FOR THE ASSIGNMENT AS
    # THOUGH IT IS COMPLETED
    shuffle(rectList)

def calcArea(rectangles):
    areaList = []
    for rect in rectangles:
        p1 = rect.getP1()
        p2 = rect.getP2()
        rectX1 = p1.getX()
        rectX2 = p2.getX()
        rectY1 = p1.getY()
        rectY2 = p2.getY()

        side1 = abs(rectX1 - rectX2)
        side2 = abs(rectY1 - rectY2)

        area = side1 * side2

        areaList.append(area)

    return areaList

def rectSort(rectangles, areas):
    for i in range(len(areas) - 1):
        count = i
        for j in range(count + 1, len(areas)):
            if areas[j] > areas[count]:
                count = j

        temp = areas[count]
        areas[count] = areas[i]
        areas[i] = temp
        temp = rectangles[count]
        rectangles[count] = rectangles[i]
        rectangles[i] = temp
    return rectangles
        


def main():
    # code to test the sorting of rectangles
    win = GraphWin("Sorting Rectangles", 300, 500)
    rectangleList = []
    populateRectangleList(rectangleList, win)
    areas = calcArea(rectangleList)
    rectSort(rectangleList, areas)
    drawRectangleList(rectangleList, win)
    
    filename = open("dataSorted.txt", "r")
    reverseSort(["cat", "dog"])
    mylist = ["hi", "bye", "hi"]
    findAndRemoveFirst(mylist, "hi")
    findAndPopFirst(mylist, "hi")
    find = readData(filename)
    
    print(isInBinary(5, find))
    
    print(isInLinear("181", find))
    print(find)
    print(selSort([20, 15, 85, 46, 23]))
    print(find)

main()


    
        
