Rows = float(input("Please Enter the Total Number of Rows : "))
Number = 1

if (Rows < 1):
    print("Please Enter a Valid Input!")
else:
    print("Floyd's Triangle")
    for i in range(1, Rows + 1):
        for j in range(1 , i + 1):
            print(Number , end = " ")
            Number = Number + 1
        print()
