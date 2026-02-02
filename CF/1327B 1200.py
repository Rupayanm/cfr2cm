for _ in range(int(input())):
    n = int(input())
    seen = set()
    res = []
    for _ in range(n):
        a = list(map(int, input().split()))
        a = a[1:]
        a = a[::-1]
        while a and a[-1] in seen:
            a.pop()
        if a:
            seen.add(a[-1])
            res.append(a[-1])
        else:
            res.append(-1)
    if len(seen) == n:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        for i in range(n):
            if res[i] == -1:
                for j in range(1, n + 1):
                    if j not in seen:
                        p = j
                        break
                print(i + 1, j)


                break
