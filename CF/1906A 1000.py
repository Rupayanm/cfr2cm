from collections import defaultdict
for _ in range(int(input())):
    S = input()
    N = len(S)

    upper = []
    lower = []

    for i in range(N):
        if S[i] == "b":
            if lower: lower.pop()
        elif S[i] == "B":
            if upper: upper.pop()
        elif S[i] < "a":
            upper.append(i)
        else:
            lower.append(i)

    ans = lower + upper
    ans.sort()
    for a in ans:
        print(S[a], end="")
    print()