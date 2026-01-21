class Solution:
    def maxLength(self, arr: List[str]) -> int:
        @lru_cache(maxsize=None)
        def gensig(ch):
            val = 0
            for i in ch:
                if val & 1<<(ord(i)-ord('a')):
                    return False
                val |= 1<<(ord(i)-ord('a'))
            return val

        @lru_cache(maxsize=None)
        def countBits(n):
            cnt = 0
            while n:
                n &= (n - 1)  # removes the lowest set bit
                cnt += 1
            return cnt
        ans = [0]

        def back(val, ind):
            if ind==len(arr):
                ans[0] = max(ans[0],countBits(val))
            for i in range(ind,len(arr)):
                if not gensig(arr[i]):
                    continue
                if val&gensig(arr[i])==0:
                    pb = val
                    val = val|gensig(arr[i])
                    back(val,i+1)
                    val = pb
            ans[0] = max(ans[0],countBits(val))

        back(0,0)
        return ans[0]


