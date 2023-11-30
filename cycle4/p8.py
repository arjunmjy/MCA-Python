def factorial(num):
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	return fact
def seriesSum(limit):
	sum=0
	for i in range(1,limit+1):
		sum=sum+((i**i)/factorial(i))
	return sum
limit=int(input("Enter the number :"))
result=seriesSum(limit)
print(f"The sum of the series  1/1! + 4/2! + 27/3! + ..... + n^n/n! upto {limit} terms is : {result}")
