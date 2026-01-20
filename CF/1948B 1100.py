for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    a = [l[-1]]
    for i in range(n-2,-1,-1):
        if l[i]>a[-1]:
            a.append(l[i]%10)
            a.append(l[i]//10)
        else:
            a.append(l[i])
    if a[::-1] == sorted(a):
        print("YES")
    else:
        print("NO")