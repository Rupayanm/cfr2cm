for i in range(int(input())):
    a,b,c=map(int,input().split())
    l1=list(map(int,input().split()))
    l1.sort()
    l2=[]
    for j in range(a):
        for k in range(a):
            l2.append(l1[0]+j*b+k*c)
    l2.sort()
    if(l1==l2):
        print('YES')
    else:
        print('NO')