class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k",
        "l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
        ans =[""]
        for i in digits:
            ch = int(i)
            curans = []
            la = len(ans)
            for ind in range(len(ans)):
                for chars in dictt[ch]:
                    ans.append(ans[ind]+chars)
            ans = ans[la:]
        if ans[0]=="":return []
        return ans