from collections import defaultdict

for i in range(int(input())):
    n = int(input())
    ans = [-1 for _ in range(n)]
    p = 1
    for j in range(0,n,2):
        ans[j] = p
        p+=1
    p =n
    for j in range(1,n,2):
        ans[j] = p
        p-=1
    print(*ans)