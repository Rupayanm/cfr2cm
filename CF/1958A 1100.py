for _ in range(int(input())):
    n,m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    lb,tb,rb,bb, tw,rw,bw,lw = 0,0,0,0,0,0,0,0
    for i in range(m):
        if grid[0][i]=="W":tw =1
        if grid[-1][i] =="W":bw = 1
        if grid[0][i] == "B": tb = 1
        if grid[-1][i] =="B":bb = 1
    for i in range(n):
        if grid[i][0]=="W":lw =1
        if grid[i][-1] =="W":rw = 1
        if grid[i][0] == "B": lb = 1
        if grid[i][-1] =="B":rb = 1
    if lw and tw and bw and rw:
        print("YES")
        continue
    if lb and tb and bb and rb:
        print("YES")
        continue
    if rw and tw and bw and lw:
        print("YES")
        continue
    if rb and tb and bb and lb:
        print("YES")
        continue
    print("NO")
