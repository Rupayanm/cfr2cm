for _ in range(int(input())):
    n  = int(input())
    s=str(input())
    ans = []
    maxi = []
    cur = 0
    for i in range(n):
        if s[i]=="L":
            cur += i
        if s[i]=="R":
            cur+=n-i-1
        if s[i]=="L" and i<n-i-1:
            maxi.append((i,n-i-1))
        if s[i]=="R" and i>n-i-1:
            maxi.append((n-i-1,i))
    maxi.sort()
    for i in range(len(maxi)):
        ans.append(cur-maxi[i][0]+maxi[i][1])
        cur = cur-maxi[i][0]+maxi[i][1]
    if maxi:
        for i in range(n-len(maxi)):
            ans.append(ans[-1])
    else:
        ans = [cur]*n
    print(*ans)