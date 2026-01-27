for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    for i in range(1,len(ai)):
        if abs(ai[i] - ai[i-1]) >=2:
            print("YES")
            print(i,i+1)
            break
    else:
        print("NO")