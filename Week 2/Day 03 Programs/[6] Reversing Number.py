Num = int(input("Enter Digits : "))
Reversed_Num = 0

while Num != 0:
    Digit = Num % 10
    Reversed_Num = Reversed_Num * 10 + Digit
    Num //= 10

print("Reversed Number : " + str(Reversed_Num))
