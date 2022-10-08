def isPalindrome(x):

	x = x.lower()
	for i in range(0, int(len(x)/2)):
		if x[i] != x[len(x)-i-1]:
			return False
	return True

s = str(input("Enter the String : "))
w = isPalindrome(s)

print(w)
if(w == True):
    print(s , "is a Palindrome")
else:
    print(s , "is Not a Palindrome")
