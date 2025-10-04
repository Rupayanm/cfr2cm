class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumk = sum(nums[:k])
        ans = sumk/k
        for right in range(k,len(nums)):
            sumk+=nums[right]
            sumk-=nums[right-k]
            ans = max(ans,sumk/k)
        return ans