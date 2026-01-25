for _ in range(int(input())):
    n = int(input())
    xi = list(map(int, input().split()))
    ai =[10000]
    for i in range(len(xi)):
        ai.append(ai[-1]+xi[i])
    print(*ai)