from collections import defaultdict

for i in range(int(input())):
    n,m,k = map(int,input().split())
    ai = list(map(int,input().split()))
    bi = list(map(int,input().split()))
    ct = defaultdict(int)
    ais = set(ai)
    bis = set(bi)
    taken = set()
    takenfromai = takenfrombi = double =  0
    for ii in range(1,k+1):
        if ii in ais and not ii in bis:
            takenfromai += 1
            continue
        if ii in bis and not ii in ais:
            takenfrombi += 1
            continue
        if ii not in bis and ii not in ais:
            print("No")
            break
    else:
        if takenfromai> k//2  or takenfrombi > k//2:
            print("No")
            continue
        print("Yes")


