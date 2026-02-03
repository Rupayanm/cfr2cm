for _ in range(int(input())):
    n=int(input())
    ai = list(map(int,input().split()))
    fl = 1
    if ai[0]>0:
        fl =1
    else:
        fl = 0
    maxp = 0
    ans = v = 0
    maxn = -1e19
    for i in range(len(ai)):
        if fl:
            if ai[i]>0:
                maxp = max(maxp, ai[i])
            else:
                fl = 0
                v += maxp
                maxp = 0
                maxn = ai[i]
        else:
            if ai[i]<0:
                maxn = max(maxn, ai[i])
            else:
                fl = 1
                v+=maxn
                maxn = -1e19
                maxp = ai[i]
    if fl:
        v+=maxp
    else:
        v+=maxn
    print(v)