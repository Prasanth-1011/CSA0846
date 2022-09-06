def pascal(x):
    for i in range(x+1):
        for j in range(x-i):
            print(" " , end = " ")

        c = 1
        for j in range(1 , i+1):
            print(c , " " , sep = " " , end = " ")
            c = c*(i-j)//j
        print()
x = int(input("Enter the Number of Rows : "))
pascal(x)
