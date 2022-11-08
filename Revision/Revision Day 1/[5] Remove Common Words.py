from collections import Counter
def removeCommonWords(Sen_1, Sen_2):
	
	Sentence_1 = list(Sen_1.split())
	Sentence_2 = list(Sen_2.split())
    
	frequency1 = Counter(Sentence_1)
	frequency2 = Counter(Sentence_2)

	word = 0

	for i in range(len(Sentence_1)):
		
    
		if Sentence_1[word] in frequency2.keys():
			Sentence_1.pop(word)
			

			word = word-1
		word += 1
	word = 0
		
	for i in range(len(Sentence_2)):
	
		if Sentence_2[word] in frequency1.keys():
			
			Sentence_2.pop(word)
			    
			word = word-1
			
		word += 1

	print(*Sentence_1)
	print(*Sentence_2)

Sentence_1 = str(input("Sentence 1 : "))
Sentence_2 = str(input("Sentence 2 : "))

removeCommonWords(Sentence_1, Sentence_2)
