from binascii import b2a_base64, a2b_base64
from math import *
from collections import *
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int,input().split()))
    dictt = Counter(ai)
    ai = list(set(ai))
    ai.sort()
    smaller = ans = 0
    for i in range(len(ai)):
        if dictt[ai[i]]>1:
            val= ((dictt[ai[i]]*(dictt[ai[i]]-1))//2)*smaller
            val+= dictt[ai[i]]*(dictt[ai[i]]-1)*(dictt[ai[i]]-2)//6
            ans += val
        smaller += dictt[ai[i]]
    print(ans)