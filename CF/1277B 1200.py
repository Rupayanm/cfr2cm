from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    vis = set()
    dictt=defaultdict(lambda : 0)
    ans = 0
    for i in range(n):
        if not dictt[ai[i]] :
            v = 0
            while not ai[i]%2 and not dictt[ai[i]]:
                ai[i] = ai[i]//2
                v+=1
            dictt[ai[i]] = v
    print(sum(dictt.values()))