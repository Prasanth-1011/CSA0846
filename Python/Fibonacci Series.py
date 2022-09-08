l = int(input("Enter the Limit : "))
a = 0
n = 1
Count = 0

if(l <= 0):
    print("Invalid Input!" "\n" "Please Enter a Positive Number")
elif(l == 1):
    print("Fibonacci Series :" , a)
else:
    print("Fibonacci Series : ")
    while(Count < l):
        print(a)
        # b = Next Term
        b = a + n
        a = n
        n = b
        Count += 1
