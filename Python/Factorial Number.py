x = int(input("Enter a Number : "))
factorial = 1
if(x<0):
    print("Factorial for Negative Number Doesn't Exist")
elif(x == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,x+1):
        factorial = factorial * i
    print("Factorial of" , x , "is" , factorial)
