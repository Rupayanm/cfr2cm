for i in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    odd = []
    even =[]
    for ii in ai:
        if ii % 2 == 0:
            even.append(ii)
        else:
            odd.append(ii)
    even.sort()
    odd.sort()
    j = 0
    ans = 0
    # print(even,odd)
    if len(odd)==0 or len(even)==0:print(0);continue
    while j<len(even):
        if even[j]>odd[-1]:
            odd[-1]+=even[-1]
            ans+=1
        else:
            odd[-1] += even[j]
            ans +=1
            j+=1
    print(ans)
