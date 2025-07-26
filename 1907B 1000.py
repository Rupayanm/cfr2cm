for _ in range(int(input())):
    smallcase = []
    uppercase = []
    s = list(str(input()))  # No need to convert to list if you're just accessing by index

    for i in range(len(s)):
        if s[i] == "b":
            if smallcase:
                smallcase.pop()
        elif s[i] == "B":
            if uppercase:
                uppercase.pop()
        elif s[i].isupper():
            uppercase.append(i)
        else:  # s[i].islower()
            smallcase.append(i)

    # Combine and sort the indices
    final_indices = smallcase + uppercase
    final_indices.sort()

    ans = ""
    for index in final_indices:
        ans += s[index]

    print(ans)