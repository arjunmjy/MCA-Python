def compare(str1,str2,n):
	s1=str1[:n]
	s2=str2[:n]
	if s1 == s2:
		return True
	else:
		return False
str1=input("Enter the first string : ")
str2=input("Enter the second string : ")
n=int(input("Enter the number : "))
print(compare(str1,str2,n))

