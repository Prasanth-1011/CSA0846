Year = int(input("Enter the Year to Check : "))

if(Year % 400 == 0):
    print(Year , "is a Leap Year")
elif(Year % 4 == 0 and Year % 100 != 0):
    print(Year , "is a Leap Year")
else:
    print(Year , "is Not a Leap Year")

Leap = Year - (Year % 4)
if(Leap % 100 == 0 and Leap % 400 != 0):
    Leap = Leap - 4
    print(Leap , "is the Previous Leap Year")
else:
    print(Leap , "is the Previous Leap Year")
