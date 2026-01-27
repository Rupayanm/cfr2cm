for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    ai = list(set(ai))
    setai = set(ai)
    ai.sort()
    v = ai[0]
    for i in range(len(ai)):
        if ai[i]%v ==0:
            setai.remove(ai[i])
    if len(setai)==0:print("Yes");continue
    ai = list(setai)
    ai.sort()
    setai = set(ai)
    v = ai[0]

    for i in range(len(ai)):
        if ai[i]%v ==0:
            setai.remove(ai[i])
    if len(setai)==0:print("Yes");continue
    print("No")