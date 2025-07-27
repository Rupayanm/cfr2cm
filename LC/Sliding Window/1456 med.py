class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        for i in range(k):
            if s[i] in "aeiou":
                vowels+=1
        i = 0
        j=k-1
        ans = vowels
        while 1:
            if s[i] in "aeiou":
                vowels-=1
            i+=1
            j+=1
            if j==len(s):
                break
            if s[j] in "aeiou":
                vowels+=1
            ans = max(ans,vowels)
        return ans