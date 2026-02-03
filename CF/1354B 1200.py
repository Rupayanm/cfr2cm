for _ in range(int(input())):
    s = input()
    cur = []
    ct = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            ct+=1
        else:
            cur.append((s[i-1],ct))
            ct = 1
    cur.append((s[-1],ct))
    # print(cur)
    ans = 1e18

    for i in range(1,len(cur)-1):
        if cur[i-1][0] != cur[i+1][0]:
            ans = min(ans, 1+cur[i][1]+1)
    if ans==1e18:
        ans = 0
    print(ans)
