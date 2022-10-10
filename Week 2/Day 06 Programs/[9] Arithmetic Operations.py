def add(a,b):
    c = a + b
    return c
def sub(a,b):
    d = a - b
    return d
def mul(a,b):
    m = a * b
    return m
def div(a,b):
    n = a / b

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
p = add(a,b)
q = sub(a,b)
r = mul(a,b)
s = div(a,b)

print("Sum =" , p)
print("Substraction =" , q)
print("Product = ", r)
print("Division =" ,s)
