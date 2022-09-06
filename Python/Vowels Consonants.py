x = input("Enter a String : ")
Vowel = 0
Conso = 0

for i in x:
    if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
        Vowel = Vowel + 1
    else:
        Conso = Conso + 1

print("The Number of Vowels in the Given String : " , Vowel)
print("The Number of Consonants in the Given String : " , Conso)
