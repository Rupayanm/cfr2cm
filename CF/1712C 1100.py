from collections import defaultdict

for _ in range(int(input())):

    n  = int(input())
    ai = list(map(int,input().split()))
    dictt= defaultdict(int)
    ms=str(n).join(map(str,ai))

    for i,v in enumerate(ai):
        dictt[v] = i
    ans = -2
    cm =0
    for i in range(1,n):
        if ans != -2 and i<ans+1:
            cm = max(cm, dictt[ai[i]],dictt[ai[i-1]])
            ans = max(ans,cm)
            continue
        cm = max(cm, dictt[ai[i - 1]])
        if ai[i]<ai[i-1]:
            ans = max(ans,cm)
    sett = set()
    for i in range(ans+1):
        sett.add(ai[i])
    print(len(sett))


