#Without Using Proper Function
x = int(input("Enter a Number : "))
order = len(str(x))
sum = 0

a = x
while(a>0):
    digit = a % 10
    sum += digit ** order
    a //= 10

if(x == sum):
    print(x , "is an Armstrong Number")
else:
    print(x , "is Not an Armstrong Number")
