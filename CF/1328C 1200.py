for _ in range(int(input())):
    n = int(input())
    x = str(input())
    first =[]
    second = []
    fl = 0
    for i in range(n):
        if fl:
            if x[i]=="2":
                second.append("2")
                first.append("0")
            if x[i] == "1":
                second.append("1")
                first.append("0")
            if x[i]=="0":
                second.append("0")
                first.append("0")
        else:
            if x[i]=="2":
                second.append("1")
                first.append("1")
            if x[i] == "1":
                second.append("0")
                first.append("1")
                fl=1
            if x[i]=="0":
                second.append("0")
                first.append("0")
    print("".join(first))
    print("".join(second))