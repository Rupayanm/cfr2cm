class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = 0
        for i in range(len(nums)):
            maxor |= nums[i]
        ans = 0
        for i in range(1<<(len(nums))):
            val = 0
            for ii in range(len(nums)):
                if (1<<ii)&i:
                    val |= nums[ii]
                if val==maxor:
                    ans+=1
                    break
        return ans