def isIsomorphic(str_1 , str_2):
    dic_str_1 = {}
    dic_str_2 = {}

    for i , value in enumerate(str_1):
        dic_str_1[value] = dic_str_1.get(value , []) + [i]

    for j , value in enumerate(str_2):
        dic_str_2[value] = dic_str_2.get(value , []) + [j]

    if sorted(dic_str_1.values()) == sorted(dic_str_2.values()):
        return True
    else:
        return False

str_1 = (input("Enter the String 1 : "))
str_2 = (input("Enter the String 2 : "))

print(isIsomorphic(str_1 , str_2))
if(isIsomorphic(str_1 , str_2) == True):
    print("The Given Strings are Isomorphic")
else:
    print("The Given Strings are Not Isomorphic")

    
