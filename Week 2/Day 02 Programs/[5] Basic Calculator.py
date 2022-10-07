print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter Choice(1/2/3/4): ")


    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))

        if choice == '1':
            print(x , "+" , y , "=" , x+y)

        elif choice == '2':
            print(x , "-" , y , "=" , x-y)

        elif choice == '3':
            print(x , "*", y, "=" , x*y)

        elif choice == '4':
            print(x , "/", y, "=" , x/y)
        
        
        a = input("Let's Do Next Calculation? (Yes/No): ")
        if a == "No":
          break
    
    else:
        print("Invalid Input")
