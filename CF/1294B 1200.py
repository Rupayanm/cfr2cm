for _ in range(int(input())):
    n = int(input())
    packages = []
    for i in range(n):
        xi,yi = map(int,input().split())
        packages.append((xi,yi))
    packages.sort()
    ans =""
    cur =(0,0)
    for i in range(len(packages)):
        xdiff = packages[i][0] - cur[0]
        ydiff = packages[i][1] - cur[1]
        if xdiff>=0 and ydiff>=0:
            cur = (packages[i][0], packages[i][1])
            ans += xdiff*"R" + ydiff*"U"
        else:
            print("NO")
            break
    else:
        print("YES")
        print(ans)