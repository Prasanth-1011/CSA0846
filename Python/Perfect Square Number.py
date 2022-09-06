import math

def isPerfecttSquare(x):
    
    if(x>=0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return false
x = int(input("Enter the Number : "))
if(isPerfecttSquare(x)):
    print("True")
else:
    print("False")
