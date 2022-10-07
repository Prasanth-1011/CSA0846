def Permutation(x , i=0):
        if(i == len(x)):
                print("".join(x))

        for j in range(i , len(x)):
                Words = [a for a in x]
                Words[i] , Words[j] = Words[j] , Words[i]
                Permutation(Words , i+1)

x = str(input("Enter the String : "))
print("The Possible Permutations are" , Permutation(x))
