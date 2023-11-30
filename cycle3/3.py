list=[]
n=int(input("Enter the number of elements in the list : "))
for i in range(n):
	num=int(input("Enter element number " + str(i+1)+" : "))
	list.append(num)
sum=0
for items in list:
	sum+=items
print(list)
print("The sum of all items in the list is : ",sum) 
