for _ in range(int(input())):
    n = int(input())
    ai=list(map(int,input().split()))
    for i,v in enumerate(ai):
        ai[i]=(v,i)
    ai.sort()
    ans = [-1]*n
    j = 0
    cur = 0
    for i in range(len(ai)):
         while j < len(ai):
             if j<=i:
                 pass
             else:
                if ai[j][0]>cur:break
             cur+=ai[j][0]
             j+=1
         ans[ai[i][1]] = j-1
    print(*ans)
