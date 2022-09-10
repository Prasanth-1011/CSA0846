import string
def ispangram(str):
    a = "abcdefghijklmnopqrstuvwxyz"
    for letter in a:
        if letter not in str.lower():
            return False
        return True

x = str(input("Enter the String : "))
if(ispangram(x) == True):
    print("The String is a Pangram")
else:
    print("The Sting is Not a Pangram")
