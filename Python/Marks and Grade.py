print("Enter Marks Obtained in 5 Subjects : ")
a = int(input("Marks Obtained in Subject 1 : "))
b = int(input("Marks Obtained in Subject 2 : "))
c = int(input("Marks Obtained in Subject 3 : "))
d = int(input("Marks Obtained in Subject 4 : "))
e = int(input("Marks Obtained in Subject 5 : "))

Total = a + b + c + d + e 
Average = Total / 5

if Average >= 91 and Average <= 100 :
    print("Your Grade is A1")
elif Average >= 81 and Average <= 90 :
    print("Your Grade is A2")
elif Average >= 71 and Average <= 80 :
    print("Your Grade is B1")
elif Average >= 61 and Average <= 70 :
    print("Your Grade is B2")
elif Average >= 51 and Average <= 60 :
    print("Your Grade is C1")
elif Average >= 41 and Average <= 50 :
    print("Your Grade is C2")
elif Average >= 0 and Average <=50 :
    print("Your Grade is D")
elif Average < 50 :
    print("Fail")
else:
    print("Invalid Input!")
