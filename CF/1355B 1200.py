import sys
for _ in range(int(input())):
	n=int(input())
	l = [int(i) for i in input().split()]
	l.sort()
	sz,ans=0,0
	for i in l:
		sz+=1
		if sz==i:
			sz=0
			ans+=1
	print(ans)