def maxArea(A, Len) :
	Area = 0
	for i in range(Len) :
		for j in range(i+1 , Len) :
			Area = max(Area, min(A[j], A[i]) * (j-i))
	return Area
a = int(input("Enter the Numbers of Elements : "))
if(a>0):
    b = []
    for i in range(0,a):
        c = int(input("Enter the Number : "))
        b.append(c)
print("Input Array = " , b)
print("Output = " , maxArea(b , a))
