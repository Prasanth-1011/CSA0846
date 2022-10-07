def MaxProfit(Price , x):

	Profit = [0] * x
    
	Max_Price = Price[x-1]

	for i in range(x-2 , 0 , -1):

		if Price[i] > Max_Price:
			Max_Price = Price[i]
		
		Profit[i] = max(Profit[i+1] , Max_Price - Price[i])
	
	Min_Price = Price[0]

	for i in range(1, x):

		if Price[i] < Min_Price:
			Min_Price = Price[i]
		
		Profit[i] = max(Profit[i-1] , Profit[i] + (Price[i] - Min_Price))

	result = Profit[x-1]
	return result

Price = [2, 30, 15, 10, 8, 25, 80]
print ("Maximum Profit is", MaxProfit(Price, len(Price)))

