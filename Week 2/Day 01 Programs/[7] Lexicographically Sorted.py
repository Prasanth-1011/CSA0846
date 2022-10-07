def countstrings(x , start):
  if(x == 0):
       return 1
  Count = 0
  for i in range(start,5):
        Count += countstrings(x-1 , i)
  return Count
def countvowelstrings(x):
        return countstrings(x , 0)
x = int(input("Enter Input : "))
print(countvowelstrings(x))
