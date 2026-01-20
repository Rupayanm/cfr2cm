from collections import defaultdict
import math


def maxSubarraySum(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    return res
p = 10**9+7
for _ in range(int(input())):
    n,k = map(int,input().split())
    ai = list(map(int,input().split()))
    maxi = maxSubarraySum(ai)
    sumarray = sum(ai)
    if maxi>0:
        print((sumarray+maxi*(2**k-1))%p)
    else:
        print(sumarray%p)
    # print(sumarray%p)
    # maxi + 2*maxi + 4*maxi