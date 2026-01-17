from collections import defaultdict
import math
for _ in range(int(input())):
    n = int(input())
    s = list(map(int,list(str(input()))))
    tct = sum(s)
    mini  = 1e19
    ct = 0
    ans = 0
    if tct>=math.ceil(n/2):
        mini = n/2
        ans = -1
    else:
        mini = abs((n/2)-n)
        ans =n-1
    # print(ans,tct)
    for i in range(n-1):
        if s[i] == 1:
            ct += 1
        peoplewantingtoliveleftinleftsection = i+1-ct
        peoplewantingtoliverightinrightsection = tct - ct
        # print(i,peoplewantingtoliveleftinleftsection,peoplewantingtoliverightinrightsection,math.ceil((i+1)/2),math.ceil((n-i-1)/2),abs((n/2)-i-1))
        if peoplewantingtoliveleftinleftsection >= math.ceil((i+1)/2) and peoplewantingtoliverightinrightsection >= math.ceil((n-i-1)/2):
            if abs((n/2)-i-1)<mini:
                mini = abs((n/2)-i-1)
                ans = i

    print(ans+1)