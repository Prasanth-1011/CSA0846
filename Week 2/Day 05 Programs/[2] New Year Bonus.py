a = input("Enter Grade : ")
try:
    b=int(input("Enter Salary : "))
    if(b>0):
        if(a == 'A'):
            if(b < 10000):
                c = b*7/100
                print("Salary :" , b)
                print("Bonus :" , c)
                print("Total to be Paid:" , b+c)
            else:
                c = b*5/100
                print("Salary :" , b)
                print("Bonus :" , c)
                print("Total to be Paid :" , b+c)
        elif(a == 'B'):
            if(b<10000):
                c = b*12/100
                print("Salary :" , b)
                print("Bonus :" , c)
                print("Total to be Paid :" , b+c)
            else:
                c = b*10/100
                print("Salary :" , b)
                print("Bonus :" , c)
                print("Total to be paid :" , b+c)
        else:
            print("Grade is Invalid\nPlease Enter a Valid Grade of the Employee")
    elif(b <= 0):
        print("Please Enter a Valid Input\nSalary Can't be Zero or Negative")
    else:
        print("Please Enter a Valid Input")
except ValueError:
    print("Invalid Input")
