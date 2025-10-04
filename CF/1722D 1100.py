for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        ans = [-1, 3] * (n // 2)
        ans[-1] = 2

    else:
        ans = [-1, 3] * (n // 2) + [-1]

    print(*ans)