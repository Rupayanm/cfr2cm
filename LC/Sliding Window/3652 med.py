def maxProfit( prices, strategy, k: int) -> int:
    pref = []
    cur = 0
    op = []
    pop = 0
    for i in range(len(prices)):
        pop += prices[i]
        op.append(pop)
        if strategy[i] == -1:
            cur -= prices[i]
        elif strategy[i] == 1:
            cur += prices[i]
        pref.append(cur)
    left = 0
    right = k - 1
    pref.append(0)
    op.append(0)
    ans = 0
    while right < len(prices):
        leftsect = pref[left - 1]
        rightsect = pref[-2] - pref[right]
        window = op[right] - op[right - k // 2]
        windowexisting = pref[right]-pref[left-1]
        ans = max(ans, leftsect + rightsect + window,leftsect+rightsect+windowexisting)
        right += 1
        left += 1
    return ans
print(maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2))