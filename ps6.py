x,y = map(int,input("Enter two numbers: ").split())
k = int(input("Enter operation: "))
if x>y:
	x = x+y
	y = x-y
	x = x-y
switch = {
	1 : x+y,
	2 : y-x,
	3 : x*y,
	4 : y/x
}
print(switch[k])

