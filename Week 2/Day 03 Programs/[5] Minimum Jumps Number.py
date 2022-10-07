def minJumps(Array, l, h):

    if (h == l):
        return 0

    if (Array[l] == 0):
        return float('inf')
 
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + Array[l] + 1):
            Jumps = minJumps(Array, i, h)
            if (Jumps != float('inf') and Jumps + 1 < min):
                min = Jumps + 1
 
    return min

Array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
x = len(Array)
print("Minimum  Number of Jumps to Reach the End Will be :", minJumps(Array , 0 , x-1))
 
