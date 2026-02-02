class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i in "+-*/":
                a=stack.pop()
                b=stack.eval(str(a)+i+str(b))pop()
                if i=="/":
                    stack.append(int(int(b)/int(a)))
                else:
                    stack.append(eval(str(b)+i+str(a)))
            else:
                stack.append(i)
        return int(stack[0])