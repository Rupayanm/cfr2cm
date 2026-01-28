for _ in range(int(input())):
    n,m = map(int,input().split())
    ai = list(map(int,input().split()))
    pi = list(map(int,input().split()))
    pi =list(pi)
    for i in range(0,len(pi)):
        pi[i] = pi[i] -1
    ais = list(sorted(ai))
    pi.sort()
    ranges = []
    start = pi[0]
    for i in range(1,len(pi)):
        if pi[i] -pi[i-1] > 1:
            ranges.append((start,pi[i-1]+1))
            start = pi[i]
    ranges.append((start,pi[-1]+1))
    for rangeo in ranges:
        ai[rangeo[0]:rangeo[1]+1] = list(sorted(ai[rangeo[0]:rangeo[1]+1]))
    if ai==ais:
        print("YES")
    else:
        print("NO")