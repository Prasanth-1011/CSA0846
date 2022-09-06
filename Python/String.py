a = input("Enter a String : ")
d = l = 0
for c in a:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1
    else:
        pass

print("Number of Digits : " , d)
print("Number of Letters : " , l)
