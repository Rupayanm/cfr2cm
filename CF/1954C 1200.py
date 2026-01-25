for _ in range(int(input())):
	x = list(input())
	y = list(input())
	fl = 0
	for i in range(len(x)):
		if fl:
			x[i],y[i] = min(x[i],y[i]),max(x[i],y[i])
			continue
		if x[i]<y[i]:
			fl = 1
			x[i],y[i] = max(x[i],y[i]), min(x[i],y[i])
		elif x[i]>y[i]:
			fl =1
	x = int(''.join(x))
	y = int(''.join(y))
	print(x,y, sep="\n")
