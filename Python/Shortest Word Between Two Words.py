x = str(input("First String : "))
y = str(input("Second Strig : "))

if len(y) > len(x):
    print("The Word With Shortest Length :" , x)
elif len(x) == len(y):
    print("Both Words" , x , "and" ,y , "Have Same Number of Letters")
else:
    print("The Word With Shortest Length :" , y)
