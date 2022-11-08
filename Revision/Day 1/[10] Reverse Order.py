x = input("Enter a String : ")
y = x.split()

y.reverse()
z = ""

for i in y:
    z += i
    z += " "
    
print("Output :" , z)
