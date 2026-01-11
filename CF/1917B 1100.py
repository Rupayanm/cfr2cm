from math import *
for _ in range(int(input())):
    n = int(input())
    s = str(input())
    ans = 0
    sett = set()
    for i in range(n):
        if s[i] not in sett:
            ans += len(s)-(i)
        sett.add(s[i])
    print(ans)