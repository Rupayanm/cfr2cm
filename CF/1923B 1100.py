import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    monsters = sorted((abs(x[i]), a[i]) for i in range(n))

    pref = 0
    ok = True

    for d, hp in monsters:
        pref += hp
        if pref > k * d:
            ok = False
            break

    print("YES" if ok else "NO")
