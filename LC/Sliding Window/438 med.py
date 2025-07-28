class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        window = [0]*26
        base = [0]*26
        ans = []
        if len(s1)>len(s2):
            return []
        for right in range(len(s1)):
            window[ord(s2[right])-ord("a")]+=1
            base[ord(s1[right])-ord("a")]+=1
        if window == base:ans.append(0)
        for right in range(len(s1),len(s2)):
            window[ord(s2[right])-ord("a")]+=1
            window[ord(s2[right-len(s1)])-ord("a")]-=1
            if window==base:ans.append(right-len(s1)+1)
        return ans
