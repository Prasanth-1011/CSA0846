x = int(input("Enter the Number of Fresh Loaves Purchased : "))
y = int(input("Enter the Number of Day Old Loaves Purchased : "))

if(x > 0):
    print("Enter a Valid Input")
elif(y > 0):
    print("Enter a Valid Input")
else:
    a =  float(input("\nRegular Price of Fresh Loaves : "))
    b =  a * (1 - 0.6)
    # Amount of New Loaves
    c = a * x
    # Amount of Day Old Leaves
    d = b * y
    # Total Amount
    e = c + d
    print("Amount of New Loaves :" , c)
    print("Amount of Day Old Loaves :" , d)
    print("Total Amount :" , e)
