
def longestNiceSubarray(nums) -> int:
    right = 1
    ans = 0
    cura = nums[0]
    curo = nums[0]
    for left in range(len(nums)):
        while right < len(nums):
            if curo & nums[right] != 0:
                break
            curo |= nums[right]
            right += 1
        ans = max(ans, right - left)
        curo &= ((1 << 31) - 1) ^ nums[left]
    return ans
print(longestNiceSubarray([1,3,8,48,10]))

