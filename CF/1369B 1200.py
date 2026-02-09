for i in range(int(input())):
    z=input()
    x=input()
    if list(x)==list(sorted(x)):
        print(x)
    else:
        print('0'*(x.index('1')+1)+'1'*(x[::-1].index('0')))