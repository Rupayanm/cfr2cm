for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ja = min(arr[:2])
    for i in range(n - 2):
        ja = max(ja, sorted(arr[i : i + 3])[1])
    print(ja)
