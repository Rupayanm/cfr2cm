from collections import *
def continuousSubarrays( nums) -> int:
    left = ans = 0
    dictt = defaultdict(int)
    for right in range(len(nums)):
        dictt[nums[right]] += 1
        keys = dictt.keys()
        while left <= right:
            maxi = max(keys)
            mini = min(keys)
            if maxi - mini > 2:
                dictt[nums[left]] -= 1
                if dictt[nums[left]] == 0:
                    del dictt[nums[left]]
                left += 1
            else:
                break
        low = right - left + 1
        ans += (low)
        print(right, low, ans)

    return ans


continuousSubarrays([5,4,2,4])