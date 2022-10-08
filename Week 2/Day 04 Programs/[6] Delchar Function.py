def delchar(x,y):
    v = ""
    for i in (x):
        if(y != i):
            v += i
    return v

a = input("Enter a String : ")
b = input("Enter Letter to Be Deleted : ")

y = delchar(a,b)
print("String After Changes : " + y)
