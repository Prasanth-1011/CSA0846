print("Enter Marks Obtained in 4 Subjects : ")
a = float(input("Marks Obtained in Subject 1 : "))
b = float(input("Marks Obtained in Subject 2 : "))
c = float(input("Marks Obtained in Subject 3 : "))
d = float(input("Marks Obtained in Subject 4 : "))

if(a < 0 or b < 0 or c < 0 or d < 0):
    print("Invalid Input")
else:
    Total = a + b + c + d
    Average = Total / 4

    if Average >= 75 :
        print("Your Grade is Distinction")
    elif Average >= 60 and Average <= 75 :
        print("Your Grade is First Division")
    elif Average >= 50 and Average <= 60 :
        print("Your Grade is Second Division")
    elif Average >= 40 and Average <= 50 :
        print("Your Grade is Third Division")
    elif Average < 50 :
        print("Fail")
    else:
        print("Invalid Input!")
