from collections import defaultdict
 
List_1 = ['12345']
print("The original list : " + str(List_1))
 
temp = defaultdict(list)
for x in List_1:
    temp[str(sorted(x))].append(x)
res = list(temp.values())
 
print("The grouped Anagrams : " + str(res))
