def maxScore(cardPoints, k: int) -> int:
    sumarray = sum(cardPoints)
    windowSize= len(cardPoints)-k
    cur = sum(cardPoints[i] for i in range(windowSize))
    ans = sumarray - cur
    for i in range(windowSize,len(cardPoints)):
        cur+=cardPoints[i]
        cur-=cardPoints[i-windowSize]
        ans = max(ans,sumarray-cur)
    return ans

print(maxScore(cardPoints = [100,40,17,9,73,75]

, k = 3))