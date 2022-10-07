from collections import defaultdict
 
test_list = str(input("String : "))
print("The Original List : " + str(test_list))
 
temp = defaultdict(list)
for i in test_list:
    temp[str(sorted(i))].append(i)
res = list(temp.values())
 
print("The Grouped Anagrams : " + str(res))
