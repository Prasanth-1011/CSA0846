def isMatch(x : str, y : str) -> bool:
    rows , columns = (len(x) , len(y))
    if(rows == 0 and columns == 0):
        return True
    if(columns == 0):
        return False
    dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
    dp[0][0] = True
    for i in range(2, columns + 1):
        if(y[i - 1] == '*'):
            dp[0][i] = dp[0][i - 2]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if(x[i - 1] == y[j - 1] or y[j - 1] == '.'):
                dp[i][j] = dp[i - 1][j - 1]
            elif j > 1 and y[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if(y[j - 2] == '.' or y[j - 2] == x[i - 1]):
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    return dp[rows][columns]
x = input("Enter First String : ")
y = input("Enter Second String : ")
print(isMatch(x , y))
