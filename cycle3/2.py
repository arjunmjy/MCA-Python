num=int(input("Enter the number of terms you want to print in the fibonacci series : "))
if num<=0:
	print("Please enter a positive number!!")
elif num==1:
	print("Fibonacci series:\n0")
else:
	print("Fibonacci series:")
	n1,n2,n3=0,1,0
	print(n1)
	print(n2)
	for i in range(2,num):
		n3=n1+n2
		print(n3)
		n1=n2
		n2=n3

