def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n_terms = int(input("Enter the number of terms you want in the fibonacci series : "))
if n_terms <= 0:
	print("Invalid input ! Please input a positive value")
else:
	print("Fibonacci series:")
	for i in range(n_terms):
		print(fibonacci(i))

