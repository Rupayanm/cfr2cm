class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums))
        nob=32
        ct = [0]*nob
        right = len(nums)-1
        for left in range(len(nums)-1,-1,-1):
            for ii in range(nob):
                if (nums[left] & (1<<ii)) >= 1:
                    ct[ii]+=1
            while 1:
                fl = 0
                for ii in range(nob):
                    if (nums[right] & (1<<ii)) >= 1:
                        if ct[ii]-1==0:
                            fl = 1
                            break
                if nums[right]==0 and left==right:fl = 1
                if fl==1:break
                else:
                    for ii in range(nob):
                        if (nums[right] & (1<<ii)) >= 1:
                            ct[ii]-=1
                    right-=1
            ans[left] = right-left+1
        return ans
