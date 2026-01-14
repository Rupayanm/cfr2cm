from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    diff = defaultdict(int)
    for i in range(1,len(ai)):
        diff[ai[i]-ai[i-1]] += 1
    ans = 1
    for i in diff:
        if i==0:
            continue

        if (n-1)//i >=1:
            v = (n-1)//i + 1
        else:
            v = 0

        ans = max(ans, min(v,diff[i]+1))
    print(ans)


