## Lab1.py
## Thomas Marshall

## This function calculates the area of a rectangle
def calcArea():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
    
def calcVolume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shootingPercentage():
    totalshots = eval(input("Enter the total amount of shots: "))
    shotsmade = eval(input("Enter how many shots were made: "))
    shootingpercentage = shotsmade/totalshots*100
    print("Shooting Percentage =", shootingpercentage, "%")

def coffee():
    pound = eval(input("Enter the number of pounds "))
    coffee = 10.50
    shipping = .86
    overhead = 1.50
    total = pound*coffee + pound*shipping + overhead
    print("Total Cost =", total)

def kilometersToMiles():
    km = eval(input("Enter the number of kilomeeters: "))
    miles = km/1.61
    print("Miles =", miles)
