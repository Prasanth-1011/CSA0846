def add_binary_nums(x , y):
		Max_Len = max(len(x) , len(y))

		x = x.zfill(Max_Len)
		y = y.zfill(Max_Len)
		
		result = ''
		
		Carry = 0

		for i in range(Max_Len - 1 , -1 , -1):
			r = Carry
			r += 1 if x[i] == '1' else 0
			r += 1 if y[i] == '1' else 0
			result += ('1' if r % 2 == 1 else '0')
			Carry = 0 if r < 2 else 1			
		if(Carry !=0):result = '1' + result

		return result.zfill(Max_Len)

print("Sum of Binary Strings :" , add_binary_nums('11' , '1'))

