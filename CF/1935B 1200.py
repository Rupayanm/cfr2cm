def func(arr,ind):
    arr[1+ind] -= 2*arr[0+ind]
    arr[2+ind] -= arr[0+ind]
    arr[0+ind] = 0
    if arr[1+ind]<0 or arr[2+ind]<0:
        return False
    # arr[-2] -= 2*arr[-1]
    # arr[-3] -= arr[-1]
    # arr[-1] = 0
    # if arr[-2]<0 or arr[-3]<0:
    #     return False
    return arr
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    for i in range(len(ai)-2):
        if func(ai,i):
            # print(ai)
            continue
        else:
            print("No")
            break
    else:
        if len(set(ai))==1 and ai[0]==0:
            print("Yes")
        else:
            print("No")
