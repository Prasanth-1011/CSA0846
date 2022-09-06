a = [1,2,3,4,5]
Even = 0
Odd = 0
Num = 0

#Using While Loop
while(Num < len(a)):
    if a[Num] % 2 == 0:
        Even += 1
    else:
        Odd += 1

    Num += 1

print("Number of Even Numbers : " , Even)
print("Number of Odd Numbers : " , Odd)
