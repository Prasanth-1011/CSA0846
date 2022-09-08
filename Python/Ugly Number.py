#Number Having 2 , 3 , 5  has its Prime Factors

def is_Ugly(x):
    if(x == 0):
        return False
    for i in [2 , 3 , 5]:
        while(x % i == 0):
            x /= i
    return x == 1

x = int(input("Enter the Number : "))
print(is_Ugly(x))
