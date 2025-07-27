from collections import Counter, defaultdict
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if total['a'] < k or total['b'] < k or total['c'] < k:
            return -1
        n = len(s)
        max_keep = 0
        left = 0
        count = defaultdict(int)
        for right in range(n):
            count[s[right]] += 1
            while left <= right and (
                    total['a'] - count['a'] < k or
                    total['b'] - count['b'] < k or
                    total['c'] - count['c'] < k
            ):
                count[s[left]] -= 1
                left += 1
            max_keep = max(max_keep, right - left + 1)

        return n - max_keep

