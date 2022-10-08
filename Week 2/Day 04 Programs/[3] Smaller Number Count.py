x = []
Num = []
Ele = int(input("Enter Total Number of Values : "))
print("Enter a Value : ")

for i in range(0,Ele):
    Value = int(input())
    Num.append(Value)

for i in range(0 , Ele):
    Count = 0
    for j in range(0 , Ele):
        if Num[i] >Num[j] and j!= i:
            Count += 1
    x.append(Count)

print(x)
