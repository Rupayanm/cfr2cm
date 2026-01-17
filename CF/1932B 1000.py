from collections import defaultdict
import math
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int,input().split()))
    time =ai[0]
    for i in range(1,len(ai)):
        if time >= ai[i]:
            v = ai[i]*math.ceil(time/ai[i])
            if v==time:
                v = ai[i]*(math.ceil(time/ai[i])+1)
            time = v
        else:
            time = ai[i]
    print(time)