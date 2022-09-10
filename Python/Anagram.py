x = str(input("Enter First String : "))
y = str(input("Enter Second String : "))

a = x.lower()
b = y.lower()

if(len(x) == len(y)):
    c = sorted(a)
    d = sorted(b)

    if(c == d):
        print(x , "and" , y , "is an Anagram")
    else:
        print(x , "and" , y , "is Not an Anagram")
else:
    print(x , "and" , y , "is Not an Anagram")
