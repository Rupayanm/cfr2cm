from collections import defaultdict

for _ in range(int(input())):
    n,k = map(int,input().split())
    ai = list(map(int,input().split()))
    dictt= defaultdict(int)
    index = defaultdict(list)
    for i in range(len(ai)):
        index[ai[i]].append(i)
    for i in range(n):
        dictt[ai[i]] += 1
    collected = 0
    sa = []
    sb = []
    for i in range(1,n+1):
        if dictt[i] == 0:
            sb.append(i)
            sb.append(i)
        if dictt[i] == 2:
            sa.append(i)
            sa.append(i)
    for i in range(1,n+1):
        if dictt[i] == 1:
            sa.append(i)
            sb.append(i)
    print(*sa[:(2*k)])
    print(*sb[:(2*k)])