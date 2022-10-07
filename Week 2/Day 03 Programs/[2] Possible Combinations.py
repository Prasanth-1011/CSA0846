x = int(input("Enter the First Number : "))
y = int(input("Enter the Second Number : "))
z = int(input("Enter the Third Number : "))

d = []
d.append(x)
d.append(y)
d.append(z)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i != j and j != k and k!= i):
                print(d[i], d[j] d[k])
