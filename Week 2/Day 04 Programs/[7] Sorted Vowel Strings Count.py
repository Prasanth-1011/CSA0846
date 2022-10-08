def CountStrings(n , Start):
    if n == 0:
        return 1
    Count = 0
    for i in range(Start, 5):
        Count += CountStrings(n - 1, i)
    return Count


def CountVowelStrings(n):
    return CountStrings(n , 0)


Value = int(input("Enter the Number of String : "))
if(Value > 0):
    print(CountVowelStrings(Value))
else:
    print("Value Can't Be Zero or Negative!")
