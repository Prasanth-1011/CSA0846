from math import factorial
x = int(input("Enter the Number of Rows : "))

for i in range(x):
    for j in range(x-i+1):
        print(end = " ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)) , end = " ")
    print()
