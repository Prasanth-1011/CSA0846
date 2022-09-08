String = str(input("Enter a Sentence : "))
Words = String.split()

Words.sort()

print("The Sorted Words are : ")
for word in Words:
    print(word)
