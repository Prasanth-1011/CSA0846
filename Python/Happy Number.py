def is_Happy_num(x):
  past = set()
  while(x != 1):
        x = sum(int(i)**2 for i in str(x))
        if(x in past):
            return False
        past.add(x)
  return True

x = int(input("Enter the Number : "))
print(is_Happy_num(x))
