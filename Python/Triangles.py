#Equilateral Triangle
#Isoscale Triangle
#Scalene Triangle
a = float(input("Enter the Length of Side 1 = "))
b = float(input("Enter the Length of Side 2 = "))
c = float(input("Enter the Length of Side 3 = "))
if(a == b and a == c):
    print("The Triangle is Isolateral")
elif(a == b or b == c or a == c):
    print("The Triangle is Isoscale")
else:
    print("The Triangle is Scalene")
