for _ in range(int(input())):
    n = int(input())
    bi = list(map(int, input().split()))
    for i in enumerate(bi):
        bi[i[0]] = (i[1],i[0])
    bi.sort()
    notthere =set(range(1,2*n+1))

    for i in range(len(bi)):
        notthere.remove(bi[i][0])
    notthere = list(notthere)
    notthere.sort()
    bi.sort(key=lambda x:x[1])
    print(bi)
    print(notthere)
    ans = [-1 for i in range(2*n)]
    for i in range(len(bi)):

    else:
        print(*ans)
