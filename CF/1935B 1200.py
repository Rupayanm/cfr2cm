from collections import *
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    dictt = Counter(ai)
    mex = -1
    fl = 0
    dp = [0] * (n + 1)
    pt = 0
    pref = []
    for i in range(n):
        dp[ai[i]] += 1
        while dp[pt]!= 0:
            pt+=1
        pref.append(pt)
    dp = [0] * (n + 1)
    pt = 0
    suff = []
    for i in range(n-1,-1,-1):
        dp[ai[i]] += 1
        while dp[pt]!= 0:
            pt+=1
        suff.append(pt)
    suff = suff[::-1]
    for i in range(n-1):
        if pref[i] == suff[i+1]:
            print(2)
            print(1,i+1)
            print(i+2,n)
            break
    else:
        print(-1)


