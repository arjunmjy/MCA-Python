n=int(input("Enter the number for the multiplication table : "))
print(f"Multiplication table for {n} is : ")
for i in range(1,11):
	product=n*i
	print(f"{n}*{i}={product}")

