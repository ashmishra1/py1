x = list(map(int,input().split()))
y = []
for i in x[:]:
	if i%2==0 :
		y.append(i)
		x.remove(i)
print(x)
print(y)