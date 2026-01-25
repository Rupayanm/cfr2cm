for i in range(int(input())):
    n,d = map(int,input().split())
    ans =[1]
    if n>=3 or d%3==0:
        ans.append(3)
    if d==5:
        ans.append(5)
    if n>=3 or d==7:
        ans.append(7)
    if n>5 or d == 9 or (n>2 and d%3 == 0):
        ans.append(9)
    print(*ans)
