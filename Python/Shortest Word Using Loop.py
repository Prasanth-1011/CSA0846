a = []
n = int(input("Enter the Number of Strings : "))
for x in range(0 , n):
    Element = input("Enter Element " + str(x+1) + " : ")
    a.append(Element)
m = len(a[0])
# Temp = t
t = a[0]

for i in a:
    if(len(i) < m):
        m = len(i)
        t = i
print("The Word With the Shortest Word :" , t)
