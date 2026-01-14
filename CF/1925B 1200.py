
# max x//n

# x= (n-1)*gcd + k*gcd
# x= gcd(n-1+k)

from math import sqrt
for _ in range(int(input())):
    x,n = map(int, input().split())
    divs = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            divs.append(i)
            if i != x // i:
                divs.append(x // i)
    divs.sort()
    for i in range(len(divs)-1,-1,-1):
        if (x-(divs[i]*(n-1)))>0 and (x-(divs[i]*(n-1)))%divs[i]==0:
            print(divs[i])
            break

