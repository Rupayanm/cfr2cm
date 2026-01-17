from collections import defaultdict

for _ in range(int(input())):
    n,k = map(int,input().split())
    ai = list(map(int,input().split()))
    dictt= defaultdict(int)
    index = defaultdict(int)
    for i in range(n):
        dictt[ai[i]] += 1
    collected = 0
    for i in range(1,n+1):
        c