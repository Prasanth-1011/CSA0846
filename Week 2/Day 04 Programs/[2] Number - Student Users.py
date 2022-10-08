Tot_User = int(input("Enter the Number of Total User : "))
Staff_User = int(input("Enter the Number Staff User : "))

if(Tot_User <= 0 or Staff_User <= 0):
    print("Enter a Valid Input!")
elif(Staff_User > Tot_User):
    print("Enter a Valid Input!")
else:
    x = Staff_User / 3
    x = x // 1
    print("Number of Student User:" , Tot_User - Staff_User - x)
