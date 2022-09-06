# Using Recursion
def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    # recursive call to the function


a = int(input("Enter a Number : "))

# call the factorial function
result = factorial(a)
        
print("Factorial of", a , "is" , result)
