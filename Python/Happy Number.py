def is_Happy_num(x):
  n = set()
  while(x != 1):
        x = sum(int(i)**2 for i in str(x))
        if(x in n):
            return False
        n.add(x)
  return True

x = int(input("Enter a Number : "))

if((is_Happy_num(x) == False)):
  print(x , "is Not a Happy Number")
else:
  print(x , "is a Happy Number")
