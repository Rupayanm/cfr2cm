n,k = map(int,input().split())
s = str(input())
ci = input().split(" ")
left = ans = 0
for right in range(n):
    if s[right] not in ci:
        tc = right - left

        ans += tc*(tc+1)//2
        left =  right + 1
tc = right -left + 1
ans += tc*(tc+1)//2
print(ans)
