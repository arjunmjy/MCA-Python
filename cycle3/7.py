n=int(input("Enter a number : "))
divisor=1
print(f"Factors of {n} :")
while divisor<=n:
	if n % divisor == 0:
		print(divisor)
	divisor+=1
