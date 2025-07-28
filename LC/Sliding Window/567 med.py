class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = [0]*26
        base = [0]*26
        if len(s1)>len(s2):
            return False
        for right in range(len(s1)):
            window[ord(s2[right])-ord("a")]+=1
            base[ord(s1[right])-ord("a")]+=1
        if window == base:return True
        for right in range(len(s1),len(s2)):
            window[ord(s2[right])-ord("a")]+=1
            window[ord(s2[right-len(s1)])-ord("a")]-=1
            if window==base:return True
        return False
