from math import *
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    odd = []
    even = []
    ans = []
    os = es = 0
    for i in range(n):
        if ai[i] % 2 != 0:
            odd.append(ai[i]%2)
            os += ai[i]
        else:
            even.append(ai[i])
            es += ai[i]
        noo = floor(len(odd)/3)
        if len(odd)%3==1 and i>0:
            noo+=1
        ans.append(os+es-noo)
    print(*ans)