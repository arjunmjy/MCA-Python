def power(lst):
	p=list(map(lambda x: 2**x,lst))
	return p
lst=[]
num=int(input("Enter the number upto where powers of 2 needed : "))
for i in range(num+1):
	lst.append(i)
lst2=power(lst)
for i in range(num+1):
	print(f"2^{i}={lst2[i]}")
