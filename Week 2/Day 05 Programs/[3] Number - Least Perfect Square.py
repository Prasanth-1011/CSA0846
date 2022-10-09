x =int(input("Enter a Number : "))
a = 0
b = 0

while(x>0):
    c = x % 10
    a = a + c
    x = x // 10

for i in range(1 , a+1):
    if(i*i <= a):
        b += 1

print("Number of Least Perfect Square Numbers :" , b)
