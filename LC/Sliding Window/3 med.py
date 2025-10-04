class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mask = 0
        i = 0
        ans = 0

        for j in range(len(s)):
            while mask & (1 << ord(s[j]) - ord("a") + 200):
                mask ^= (1 << (ord(s[i]) - ord("a") + 200))
                i += 1
            mask |= 1 << (ord(s[j]) - ord("a") + 200)
            ans = max(ans, j - i + 1)
        return ans 
