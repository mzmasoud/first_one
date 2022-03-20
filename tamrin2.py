import decimal
# newyon method for square root

number = int(input("plz enter the number"))
nsquare = float(input("plz enter the number you think it is near to the root"))

def square_root (n,g):

	root = 0.5 * (g + (n / g))
	root = decimal.Decimal(root)

	return root

x = square_root(number,nsquare)

print(x)


		
	




