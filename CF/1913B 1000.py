for _ in range(int(input())):
    s = str(input())
    ct0 = s.count('0')
    ct1 = s.count('1')
    j=0
    while ct0!=0 or ct1!=0:
        if s[j] == '0':
            ct1-=1
        else:
            ct0-=1
        if ct0<0 or ct1<0:
            ct1+=1
            break
        j+=1
    print(ct0+ct1)