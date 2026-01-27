from collections import *
for i in range(int(input())):
    q = str(input())
    ct = Counter(q)
    if ct["U"]>ct["D"]:
        ct["U"] -= ct["U"] - ct["D"]
    elif ct["U"]<ct["D"]:
        ct["D"] -= ct["D"] - ct["U"]
    if ct["L"]>ct["R"]:
        ct["L"] -= ct["L"] - ct["R"]
    elif ct["L"]<ct["R"]:
        ct["R"] -= ct["R"] - ct["L"]
    ans = "U"*ct["U"] + "L"*ct["L"] + "D"*ct["D"]  + "R"*ct["R"]
    if not ct["L"] and ans:
        ans = "UD"
    if not ct["U"] and ans:
        ans = "RL"
    print(len(ans))
    print(ans)