#this program is to function as the summation function (∑)

#definitions of the math functions
def sigma_func(int(variable),int(lower),int(upper)):
	total = 0
	for lower in upper:
		total += variable
	return total

def py_func(int(variable),int(lower),int(upper)):
	product = 0
	for lower in upper:
		product *= variable
	return product

#input sequence
choice = input("Sum(∑) or product(∏)?: ")
choice = choice.lower()
if choice == "sum":
	test_var = input("Number to sum: ")
elif choice == "product":
	test_var = input("Number to compound: ")
test_lower = input("Lower bound: ")
test_upper = input("Upper bound: ")

#runnign the functions
if choice == "sum":
	print(sigma_func(test_var,test_lower,test_upper))
elif choice == "product":
	print(py_func(test_var,test_lower,test_upper))