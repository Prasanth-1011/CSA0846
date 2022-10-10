def pascal(x):
    for i in range(x+1):
        for j in range(x-i):
            print(" " , end = " ")

        c = 1
        for j in range(1 , i+1):
            print(c , " " , sep = " " , end = " ")
            c = c*(i-j)//j
        print()
        
x = int(input("Enter the Number of Rows : "))
if(x <=0 ):
    print("Enter a Valid Input!")
else:
    pascal(x)
    b = int(input("\nEnter the Row : "))
    from math import factorial
    if(b>0):
        a = 0
        for i in range(x):
            for j in range(i+1):
                if(i == b-1):
                    a += factorial(i) // (factorial(j) * factorial(i-j))
        print("Sum of Elements in" , b , "Row :" , a)
    else:
        print("Invalid Input")
