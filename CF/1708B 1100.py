for _ in range(int(input())):
    n, l, r = map(int,input().split())
    ans = []
    for i in range(1,n+1):
        if l%i==0:
            ans.append(l)
        else:
            v1= i*(l//i)+i
            if v1>r:
                print("NO")
                break
            else:
                ans.append(v1)
    else:
        print("Yes")
        print(*ans)