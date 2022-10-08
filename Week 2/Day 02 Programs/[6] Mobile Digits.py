HashTable = ["" , "" , "abc" , "def" , "ghi" , "jkl" , "mno" , "pqrs" , "tuv" , "wxyz"]

def printWordsUtil(Number, Curr, output, x):
	if(Curr == x):
		print(output)
		return

	for i in range(len(HashTable[Number[Curr]])):
		output.append(HashTable[Number[Curr]][i])
		printWordsUtil(Number, Curr + 1, output, x)
		output.pop()
		if(Number[Curr] == 0 or Number[Curr] == 1):
			return
g = []
h = int(input("Enter the Number of Elements : "))

for i in range (0 , h):
    k = int(input())
    g.append(k)
            
def printWords(Number, x):
	printWordsUtil(Number, 0, [], x)

if __name__ == '__main__':
	
	Number = g
	x = len(Number)

	# Function call
	printWords(Number , x)
