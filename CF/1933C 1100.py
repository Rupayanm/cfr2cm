t = int(input())
for _ in range(t):
    a, b, l = map(int, input().split())
    s = set()
    for x in range(21):
        for y in range(21):
            if l % (a ** x * b ** y) == 0:
                s.add(l // (a ** x * b ** y))
    print(len(s))