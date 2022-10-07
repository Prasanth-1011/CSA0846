def fib(x):
    if(x <= 1):
        return x
    return fib(x-1)+fib(x-2)
def countways(s):
    return fib(s+1)
x = int(input("Enter a Number : "))
print("Number of Ways :" , (countways(x)))
