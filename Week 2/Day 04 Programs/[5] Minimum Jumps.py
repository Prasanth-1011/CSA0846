x = []
Ele = int(input("Enter the Number of Elements : "))
print("Enter the Value : ")

for i in range(0 , Ele):
    Value = int(input())
    x.append(Value)

f = 0
Count = 0
try:
    while True:
        if Count + x[f] == len(x):
            print(Count)
            break
        if Count + x[f] == len(x) - 1:
            print(Count + 1)
            break
        if Count + x[f]+1== len(x)-1:
            print(Count + 2)
            break

        f += 1
        Count += 1
except:
    print("End isn’t Reachable!")
