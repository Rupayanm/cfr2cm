# k^x + k^y + k^z = a[i]   #if it takes more than 1 value i need to compensate it with a 0 else where

for _ in range(int(input())):
    n,k = map(int,input().split())
    ai = list(map(int,input().split()))
    val = []
    ai.sort()
    ind = 0
    for i in range(len(ai)):
        if ai[i]!=0:
            ind = i
            break
    ai = ai[ind:]
    for i in range(len(ai)):
        cur = []
        for ii in range(55,-1,-1):
            if ai[i]>=pow(k,ii):
                cur.append(ii)
                ai[i] -= pow(k,ii)
                if ai[i]<=0:
                    break
        if not ai[i]:
            val.append(cur)
        else:
            print("No")
            break
    else:
        sett =set()
        for i in val:
            for ii in i:
                if ii in sett :
                    print("No")
                    break
                else:sett.add(ii)
            else:
                continue
            break
        else:
            print("Yes")