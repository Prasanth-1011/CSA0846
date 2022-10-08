def value(r):
    if(r == 'I'):
        return 1
    if(r == 'V'):
        return 5
    if(r == 'X'):
        return 10
    if(r == 'L'):
        return 50
    if(r == 'C'):
       return 100
    if(r == 'D'):
        return 500
    if(r == 'M'):
        return 1000
    return -1
def romantodecimal(str):
    x = 0
    i = 0
    while (i < len(str)):
        S1 = value(str[i])
        if(i+1 < len(str)):
            S2 = value(str[i+1])
            if(S1 >= S2):
                x = x + S1
                i = i + 1
            else:
                x = x + S2 -S1
                i = i + 2
        else:
            x = x + S1
            i = i+1
    return x
Message = str(input("Enter a Value in Roman : "))
try:
    n = romantodecimal(Message)
    if n > 3999:
        raise Exception()
    print(n)
except Exception:
    print("Please Enter a Valid Input!")
