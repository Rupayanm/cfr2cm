from collections import *
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        ct = defaultdict(int)
        ans = 1e18
        astr=""
        left = 0
        for right in range(len(s)):
            ct[s[right]]+=1
            while 1:
                for key in target:
                    if ct[key]<target[key]:
                        break
                else:
                    ct[s[left]]-=1
                    if (right-left+1)<ans:
                        astr=s[left:right+1]
                    ans = min(ans,right-left+1)
                    left+=1
                    continue
                break
        return astr
a=Solution()
print(a.minWindow(s = "a", t = "aa"))