for _ in range(int(input())):
    n, k = map(int, input().split())
    if n >= k and ((n & 1 and k & 1) or (not n & 1 and not k & 1)):
        print('YES')
        print(*[1] * (k - 1), n - k + 1)
    elif n >= 2 * k and not n & 1:
        print('YES')
        print(*[2] * (k - 1), n - 2 * k + 2)
    else:
        print('NO')
