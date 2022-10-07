l = []
N = int(input("Enter Number of Elements : "))
for i in range (0 , N):
    print("Enter the Elements" , format(i+1) , ":" " ")
    M = int(input())
    l.append(M)
print("The Entered List is : " , l)
def sum_squares(l):
    Odd = 0
    Even = 0
    for i in l:
        if(i % 2 == 0):
            Even += i**2
        else:
            Odd += i**2
    l=[Odd , Even]
    return(l)
print(sum_squares(l))
