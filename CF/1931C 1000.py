from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    ai = list(map(int,input().split()))
    leftwindow = 1
    rightwindow = 1
    for i in range(1,n):
        if ai[i] == ai[i-1]:
            leftwindow += 1
        else:break
    for i in range(n-2,-1,-1):
        if ai[i] == ai[i+1]:
            rightwindow += 1
        else:
            break
    if len(set(ai))==1:
        print(0)
        continue
    if ai[0]==ai[-1]:
        print(n-leftwindow-rightwindow)
        continue
    else:
        print(n-max(leftwindow,rightwindow))