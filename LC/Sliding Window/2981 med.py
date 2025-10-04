class Solution:
    def maximumLength(self, s: str) -> int:
        dictt = defaultdict(list)
        ct = 1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                dictt[s[i-1]].append(ct)
                ct=1
            else:
                ct+=1
        dictt[s[-1]].append(ct)
        ans = -1
        for ch in dictt:
            dictt[ch].sort()
            if dictt[ch][-1]>2:
                ans = max(ans, dictt[ch][-1]-2)
            if len(dictt[ch])>1 and dictt[ch][-2]<dictt[ch][-1]:
                ans = max(ans, dictt[ch][-2])
            if len(dictt[ch])>1 and  dictt[ch][-2]==dictt[ch][-1]:
                ans = max(ans, dictt[ch][-1]-1)
            if len(dictt[ch])>2:
                ans = max(ans,dictt[ch][-3])
        if ans==0:ans=-1
        return ans
