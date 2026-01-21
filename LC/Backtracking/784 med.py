class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans =[]
        def func(cur, ind):
            if len(cur)>4:return
            if ind==len(s):
                if len(cur)==4:
                    ans.append(".".join(cur))
                else:
                    return
            for i in range(ind+1,len(s)+1):
                string = str(s[ind:i])
                if (string[0]=='0' and len(string)>1) or int(string)>255 :
                    break
                else:
                    cur.append(string)
                    func(cur,i)
                    cur.pop()
        func([],0)
        return ans

