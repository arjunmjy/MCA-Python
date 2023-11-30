n=int(input("Enter a number : "))
x=n
y=0
while x != 0:
	x //= 10
	y += 1
t=n
armstrong_sum=0
while t>0:
	digit=t%10
	armstrong_sum+=digit**y
	t//=10
if n==armstrong_sum:
	print(n," is an armstrong number")
else:
	print(n," is not an armstrong number")
