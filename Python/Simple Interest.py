def simple_interest(p , t , r):
    print("Principal Amount : " , p)
    print("Time Period : " , t)
    print("Rate of Interest : " , r)

    si = (p * t * r) / 100
    print("\n")
    print("Simple Interest : " , si)
    return si

simple_interest(8 , 7 , 8)
