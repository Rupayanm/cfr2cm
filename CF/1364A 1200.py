t=int(input())
while(t):
    t=t-1
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    ans=-1
    sum=0
    for i in range(len(a)):
        sum+=a[i]
        if sum%x:
            ans=max(ans,max(len(a)-i-1,i+1))
    print(ans)