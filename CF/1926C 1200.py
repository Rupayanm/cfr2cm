def sumdig(num):
    val = 0
    while num:
        v = num % 10
        val+=v
        num = num//10
    return val
ans = [0,1]
for i in range(2,5*10**5):
    ans.append(ans[-1]+sumdig(i))
for i in range(int(input())):
    n = int(input())
    print(ans[n])