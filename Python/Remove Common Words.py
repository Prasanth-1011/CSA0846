from collections import Counter
def removeCommonWords(Sent_1, Sent_2):
	
	Sen_1 = list(Sent_1.split())
	Sen_2 = list(Sent_2.split())
	
	Fre_1 = Counter(Sen_1)
	Fre_2 = Counter(Sen_2)

	Word = 0
	
	for i in range(len(Sen_1)):
		
		if Sen_1[Word] in Fre_2.keys():
			
			Sen_1.pop(Word)			
			Word = Word - 1
		Word += 1
	Word = 0
	
	for i in range(len(Sen_2)):
		if Sen_2[Word] in Fre_1.keys():
			
			Sen_2.pop(Word)
			Word = Word - 1
		Word += 1
	
	print(*Sen_1)
	print(*Sen_2)

Sen_1 = str(input("Enter the Sentence 1 : "))
Sen_2 = str(input("Enter the Sentence 2 : "))

removeCommonWords(Sen_1, Sen_2)
