Year = int(input("Enter the Year to Check : "))
if (Year % 100 == 0 and Year % 400 == 0):
    print(Year , " is a Leap Year")
    Leap_Year = Year
elif(Year % 4 == 0 and Year % 100 != 0):
    print(Year , "is a Leap Year")
    Leap_Year = Year
else:
    print(Year , "is Not a Leap Year")
S = (Year % 4)
if(Year % 4 == 0):
    S = 4
else:
    S = S
P = Year - S
if(P % 100 == 0):
    P = P - 4
    print(P , "is the Previous Leap Year")
elif(P % 400 == 0):
    print(P , "is the Previous Leap Year")
else:
    print(P , "is the Previous Leap Year")
R = 4 - (Year % 4)
Q = Year + R
if(Q % 100 == 0 and Q % 400 != 0):
    Q = Q + 4
    print(Q , "is the Next Leap Year")
else:
    print(Q , "is the Next Leap Year")
