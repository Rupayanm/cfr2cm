def calc(l, r):
    val = 0
    length = r - l + 1
    for i in range(nob):
        if dp[r][i] - dp[l-1][i] == length:
            val |= (1 << i)
    return val


for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))

    nob = 5
    dp = [[0]*nob for _ in range(n+1)]

    # build prefix dp (1-indexed)
    for i in range(1, n+1):
        for b in range(nob):
            dp[i][b] = dp[i-1][b]
            if ai[i-1] & (1 << b):
                dp[i][b] += 1

    q = int(input())
    for _ in range(q):
        l, k = map(int, input().split())
        # convert to 1-indexed
        l = l

        lo, hi = l, n
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if calc(l, mid) >= k:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        print(ans, )
