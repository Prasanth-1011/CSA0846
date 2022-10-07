def solve(Numbers):
   Count = 0
   a =len(Numbers)
   for i in range(a):
      for j in range(i+1 , a):
         if Numbers[i] == Numbers[j]:
            Count += 1
   return Count

Numbers = [1,1,1,1]
print(solve(Numbers))
