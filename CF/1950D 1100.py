for _ in range(int(input())):
	n=int(input())
	for i in range(5):
		for i in range(32,1,-1):
			if n%int(bin(i)[2:])==0:
				n=n//int(bin(i)[2:])
	if n==1:print("YES")
	else:print("NO")