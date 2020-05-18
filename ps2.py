x = input()
ls = []
for i in range(len(x)):
	ls.append(x[i])
ls.sort(reverse=True)
print(''.join(ls))