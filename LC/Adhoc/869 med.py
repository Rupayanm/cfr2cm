from collections import *
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ns=str(n)
        cur=1
        ct=Counter(ns)
        while len(str(cur))<=len(ns):
            if len(str(cur))==len(ns):
                if Counter(str(cur))==ct:return True
            cur*=2
        return False