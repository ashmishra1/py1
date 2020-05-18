def outer(a,b):
	c=0
	def inner():
		outer.c = a + b
	inner()
	return outer.c+5

x = int(input())
y = int(input())
print(outer(x,y))