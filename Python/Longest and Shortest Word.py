x = str(input("First String : "))
y = str(input("Second Strig : "))

if len(x) > len(y):
    print("The Word With Longest Length :" , x)
    print("The Word With Shortest Length :" , y)
elif len(x) == len(y):
    print("Both Words" , x , "and" ,y , "Have Same Number of Letters")
else:
    print("The Word With Longest Length :" , y)
    print("The Word With Shortest Length :" , x)
