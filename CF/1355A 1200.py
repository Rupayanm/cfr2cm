for _ in range(int(input())):
    v, k = input().split()
    k = int(k)

    for _ in range(k - 1):   # perform k-1 operations
        digits = list(map(int, v))
        mini = min(digits)
        maxi = max(digits)

        if mini == 0:
            break

        v = str(int(v) + mini * maxi)

    print(v)
