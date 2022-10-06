Number = int(input("Enter a Number Till Needed to Check : "))

primes = []
for i in range (2 , Number + 1):
    for j in range (2 , i):
        if(i%j == 0):
            break
    else:
        primes.append(i)
print(primes)
