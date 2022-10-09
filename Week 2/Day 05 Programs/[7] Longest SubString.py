def LongestSubstring(s, k) :
    Ans = 0
    Fre = [0]*26
    n = len(s)

    for i in range(n) :
        Fre[ord(s[i]) - ord('a')] += 1
    unique = 0

    for i in range(26) :
        if (Fre[i] != 0) :
            unique += 1

    for Curr_Unique in range(1, unique + 1) :
        Fre = [0]*26
        Start, End = 0, 0

        Cnt, Count_k = 0, 0

        while (End < n) :
            if (Cnt <= Curr_Unique) :
                Ind = ord(s[End]) - ord('a')

                if (Fre[Ind] == 0) :
                    Cnt += 1
                Fre[Ind] += 1

                if (Fre[Ind] == k) :
                    Count_k += 1
                End += 1

            else :
                Ind = ord(s[Start]) - ord('a')

                if (Fre[Ind] == k) :
                    Count_k -= 1
                Fre[Ind] -= 1

                if (Fre[Ind] == 0) :
                    Cnt -= 1

                Start += 1

            if ((Cnt == Curr_Unique) and (Count_k == Curr_Unique)) :
                Ans = max(Ans, End - Start)
    print("Output :" , Ans)

S = input("Enter the String : ")
K = int(input("Enter the Value of K : "))

LongestSubstring(S, K)
