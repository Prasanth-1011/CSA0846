Rows = int(input("Enter the Number of Rows : "))
print("The Output Sequence Be Like : ")

for i in range (1 , Rows + 1):
    if(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    elif(i % 3 == 0 and i % 5 == 0):
        print("Fizz Buzz")
    else:
        print(i)
