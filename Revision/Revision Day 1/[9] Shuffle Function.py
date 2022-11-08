def shuffle(x,y):
    a = len(x)
    e = len(y)
    z = a + e
    for i in range(z):
        if(i < a):
            d.append(b[i])
        if(i < e):
            d.append(f[i])
    print("Shuffled list :" , d)

a = int(input("Enter Number of Elements of x : "))
b = []
d = []

for i in range(a):
    c = int(input("Enter Element : "))
    b.append(c)

e = int(input("Enter Number of Elements of y : "))
f = []
for i in range(e):
    g = int(input("Enter Element : "))
    f.append(g)

shuffle(b,f)
