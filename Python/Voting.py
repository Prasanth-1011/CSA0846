a = str(input("Enter the Name : "))
b = int(input("Enter the Age of the Person : "))
c = 18 - b

if(b>=18):
    print("The Candidate" , a , "is Eligible for Voting")
else:
    print("The Candidate" , a , "is Not Eligible for Voting")
    print("The Candidate can Vote After" , c , "Year")
    
