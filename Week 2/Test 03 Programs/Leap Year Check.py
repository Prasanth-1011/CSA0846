Year = int(input("Enter the Year to Check : "))

if(Year % 100 == 0 and Year % 400 == 0):
    print(Year , "is a Leap Year")
elif(Year % 4 == 0 and Year % 100 != 0):
    print(Year , "is a Leap Year")
else:
    print(Year , "is Not a Leap Year")
