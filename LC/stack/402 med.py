class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sys.set_int_max_str_digits(10**5)
        stack = []
        for i in range(len(num)):
            while stack and k and int(num[i])<stack[-1]:
                stack.pop()
                k-=1
            stack.append(int(num[i]))
        ans = 0
        for ii in stack:
            ans*=10
            ans+=ii
        ans = str(ans)
        if k:
            ans = ans[:len(ans)-k]
            if not ans:
                ans = "0"
        return str(ans)