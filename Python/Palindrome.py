def ispalindrome(s):
    return s == s[::-1]

s = input("Enter a String : ")
w = ispalindrome(s)

if w:
    print("The Given String" , s , "is a Palindrome")
else:
    print("The Given String" , s , "is Not a Palindrome")
