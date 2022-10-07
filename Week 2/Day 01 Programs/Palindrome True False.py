def isPalindrome(str):

	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = str(input("Enter the String : "))
w = isPalindrome(s)

print(w)
if(w == True):
    print(s , "is a Palindrome")
else:
    print(s , "is Not a Palindrome")
