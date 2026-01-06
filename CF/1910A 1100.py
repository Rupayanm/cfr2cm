for _ in range(int(input())):
    s = str(input())
    for j in range(len(s)-1,-1,-1):
        if s[j] == "0":
            continue

        print(s[0:j])
        break