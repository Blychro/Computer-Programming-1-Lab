
## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: Thomas Marshall 
import math
# This is a sample function to show how to "comment out" function calls
def helloWorld():
    print("Hello, world!")

# This function adds multiples of threes up to and including an upper bound
#Complete
def sumOfThrees():
    print("This function sums multiples of three.")
    up = eval(input("Enter the upper bound: "))
    total = 0
    
    for i in range(3,up+1,3):
        total = total + i
    print("Total sum =", total)

#Complete
def triangleArea():
    print("This program will calculate the area of a triangle.")
    a = eval(input("Enter the first side: "))
    b = eval(input("Enter the second side: "))
    c = eval(input("Enter the third side: "))
    s = (a+b+c)/2
    A = math.sqrt(s*(s - a)*(s - b)*(s - c))
    print("Area =", A)

#Complete
def sumSquares():
    total = 0
    down = eval(input("Enter the lower bound: "))
    up = eval(input("Enter the upper bound: "))
    for i in range(down,(up+1),1):
        total = total + i**2
    print(total)
    
#Complete
def power():
    total = 1
    base = eval(input("Enter the base: "))
    exp = eval(input("Enter the exponent: "))
    for i in range(exp):
        total = total*base
        
    print(base, "^", exp, "=", total)
    

    
#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above, and a call to this function
#is commented out below.

def main():
    #helloWorld()  
    sumOfThrees()





    
    

    

    

