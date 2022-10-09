a = int(input("Enter List of Elements : "))
c = []
d = []

for i in range(a):
    b = int(input("Enter Element : "))
    c.append(b)

d = c.copy()
print("Input :" , d)
c.sort()

for i in range(0,a):
    if(c[a-1] == d[i]):
        f = i
print("Output :" , f)
