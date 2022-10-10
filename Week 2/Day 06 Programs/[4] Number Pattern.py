r = int(input("Enter the Number of Rows : "))

if(r<1):
    print("Invalid Input")
else:
    for i in range(1 , r+1):
        for j in range(1 , i+1):
            print(j , " " , end = "")
        print("\n")
