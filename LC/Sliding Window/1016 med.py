class Solution:
    def queryString(self, s: str, n: int) -> bool:
        dictt = defaultdict(int)
        for left in range(len(s)):
            cur = 0
            for right in range(left,len(s)):
                cur*=2
                if s[right]=='1':
                    cur+=1
                dictt[cur]+=1
        ks = list(dictt.keys()).copy()
        for i in ks:
            if i>n:
                del dictt[i]
        if 0 in dictt:
            del dictt[0]
        return len(dictt)==n