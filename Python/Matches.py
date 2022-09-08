x = str(input("Enter First String : "))
y = str(input("Enter Scond String : "))

a = len(x)
count = 0

for i in range(a):
    if(x[i] == y[i]):
        count += 1

print("Number of Matches :" , count)
