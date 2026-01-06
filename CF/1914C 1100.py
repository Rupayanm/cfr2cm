for _ in range(int(input())):
    n,k = map(int,input().split())
    ai = list(map(int,input().split()))
    bi = list(map(int,input().split()))
    cm = 0
    ans = 0
    pref = 0
    for i in range(len(ai)):
        cm = max(cm, bi[i])
        pref += ai[i]
        totake = k-(i+1)
        if totake<0:break
        else:
            ans = max(ans, cm*totake+pref)
    print(ans)
