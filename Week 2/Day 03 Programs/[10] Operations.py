def EditDistance(Str_1 , Str_2 , m , n):
    
    if m == 0:
        return n
   
    if n == 0:
        return m
    
    if Str_1[m-1] == Str_2[n-1]:
        return EditDistance(Str_1 , Str_2 , m-1 , n-1)
    
    return 1 + min(EditDistance(Str_1 , Str_2 , m , n-1), EditDistance(Str_1 , Str_2 , m-1 , n) , EditDistance(Str_1 , Str_2 , m-1 , n-1))

Str_1 = input("Enter Word 1 : ")
Str_2 = input("Enter Word 2 : ")
print (EditDistance(Str_1, Str_2, len(Str_1), len(Str_2)))
