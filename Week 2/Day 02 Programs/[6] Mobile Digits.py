Letters = {"2": "abc" , "3": "def" , "4": "ghi" , "5": "jkl" , "6": "mno" , "7": "pqrs" , "8": "tuv" , "9": "wxyz"}
x = []
Value = input("Enter the Digit: ")
try:
    if len(Value) == 2:
        for i in range(0 , len(Value)):
            New_Value = Letters[Value[i]]
            x = (New_Value)
        print("[" , end = '')
        for i in x[0]:
            for j in x[1]:
                print("\"" , i+j , "\"" , end = ",")

        print("]" , end = '')

    if len(Value) == 1:
        print("[" , end = '')
        for i in Letters:
            print("\"" , i , "\"" , end = ',')
        print("]" , end = '')
except:
    print("]")
