
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack(start: int):
            if len(cur) == k:
                ans.append(cur[:])
                return
            if len(cur) + (n - start + 1) < k:
                return
            for i in range(start, n+1):
                cur.append(i)
                backtrack(i+1)
                cur.pop()

        backtrack(1)
        return ans
