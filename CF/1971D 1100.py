for _ in range(int(input())):
    s = str(input())
    ps = 0
    zo = 0
    oz = 0
    curz = curo = 0
    for i in range(1,len(s)):
        if s[i] == '0' and s[i-1] == '1':
            oz += 1
        elif s[i] == '0' and s[i-1] == '0':
            curo  += 1
        elif s[i] == '1' and s[i-1] == '0':
            zo += 1
        elif s[i] == '1' and s[i-1] == '1':
            curz += 1
    # print(oz,zo)
    print(oz + max(0,zo-1)+1)