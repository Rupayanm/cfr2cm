class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        def func(size):
            windowSum = 0
            ra = []
            for i in range(len(nums)):
                windowSum+=nums[i]
                if i>=size:
                    windowSum-=nums[i-size]
                if i>=size-1:
                    ra.append(windowSum)
                    continue
                ra.append(-1)
            pref=[-1]*(len(ra))
            pref[-1]=ra[-1]
            for i in range(len(pref)-2,-1,-1):
                pref[i] = max(pref[i+1], ra[i])
            return ra, pref
        first,firstPref = func(firstLen)
        sec,secPref = func(secondLen)
        ans = 0
        for i in range(len(first)):
            if i+secondLen<len(secPref):
                ans = max(ans, first[i]+secPref[i+secondLen])
        for i in range(len(sec)):
            if i+firstLen<len(firstPref):
                ans = max(ans, sec[i]+firstPref[i+firstLen])
        return(ans)

a= Solution()
print(a.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8]
, firstLen = 4, secondLen = 3))


