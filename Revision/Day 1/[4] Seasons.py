Day = input("Enter Month and Date : ")

Month = Day.split()[0]
Date = Day.split()[1]

if Month in ('September' , 'October' , 'November'):
	print("Season is Spring")

elif Month in ('January' , 'Febraury' , 'December'):
	print("Season is Fall")

elif Month in ('March', 'April', 'May'):
	print("Season is Summer")

elif Month in ('June','July','August'):
    print("Season is Winter")
