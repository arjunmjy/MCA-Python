def odd_even(num):
	if num % 2 == 0:
		return f"{num} is an even number"
	else:
		return f"{num} is an odd number"
num=int(input("Enter a number to check whether it is even or odd :"))
result=odd_even(num)
print(result)
