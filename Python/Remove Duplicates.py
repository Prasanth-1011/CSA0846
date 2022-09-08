a = [1 , 1 , 2 , 3 , 3 , 10 , 30]
b = [2 , 2 , 4 , 5 , 7 , 70 , 45]

c = list(set(a))
print("List 1 :" , a)
print("List 1 After Removing Duplicates :" , c)
print("\n")
d = list(set(b))
print("List 2 :" , b)
print("List 2 After Removing Duplicates :" , d)
print("\n")

#Symmetric Difference
print("Symmetric Difference :" , set(c) ^ set(d))
