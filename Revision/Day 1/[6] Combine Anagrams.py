from collections import defaultdict

def Print_Anagrams_Together(Words):
    Grouped_Words = defaultdict(list)

    for Word in Words:
        Grouped_Words[" ".join(sorted(Word))].append(Word)

    for Group in Grouped_Words.values():
        print(" ".join(Group))

if __name__ == "__main__":
    a = []
    b = int(input("Enter the Number of String : "))
    for i in range (b):
        c = str(input("Enter the String : "))
        a.append(c)

    Print_Anagrams_Together(a)
