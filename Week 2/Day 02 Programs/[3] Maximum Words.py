def word_count(x):
    max_space = 0
    for i in range(0 , len(x)):
        word = x[i]
        new_count = 0
        for j in range(0 , len(word)):
            if word[j] == ' ':
                new_count += 1

        if(new_count > max_space):
            max_space = new_count

    return max_space

l=[]
count = int(input("Enter the Full Sentences: "))
print("Enter the Sentences : ")
for i in range(0 , count):
    val=input()
    l.append(val)
counted=word_count(l)
print("Maximum Number of Words: " , counted+1)
