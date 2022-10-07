E = []
L = []
t = int(input(" T = "))
try:
    if(t>0):
        for i in range(t):
            e = int(input("Guest Entered Inside = "))
            E.append(e)
        for i in range(t):
            l = int(input("Guest Leaved Outside = "))
            L.append(l)
        S = 0
        M = 0
        for i in range(t):
            S += E[i] - L[i]
            M = max(S , M)
        print(" E = " , E)
        print(" L = " , L)
        print("Output : " , M)
    else:
        print("Inavalid Value")
except ValueError:
    print("Enter All Values : ")
