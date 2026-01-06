for _ in range(int(input())):
    # n,k = map(int,input().split())
    n=int(input())
    ai=list(enumerate(list(map(int,input().split()))))
    bi=list(enumerate(list(map(int,input().split()))))
    ci=list(enumerate(list(map(int,input().split()))))
    ai.sort(key=lambda i:i[1],reverse=True);bi.sort(key=lambda i:i[1],reverse=True);ci.sort(key=lambda i:i[1],reverse=True)
    ans=0
    for i in range(3):
        for ii in range(3):
            for iii in range(3):
                sett={ai[i][0],bi[ii][0],ci[iii][0]}
                if len(sett)==3:
                    ans=max(ans,ai[i][1]+bi[ii][1]+ci[iii][1])
    print(ans)