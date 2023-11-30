def square(a):
	area=a*a
	print("The area of the square is : ",area)
def rectangle(l,b):
	area=l*b
	print("The area of the rectangle is : ",area)
def triangle(base,height):
	area=0.5*base*height
	print("The area of the triangle is : ",area)
a=int(input("\nSquare\nEnter the side length of square : "))
square(a)
l=int(input("\nRectangle\nEnter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
rectangle(l,b)
base=int(input("\nTriangle\nEnter the base length of triangle : "))
height=int(input("Enter the height of the triangle : "))
triangle(base,height)
