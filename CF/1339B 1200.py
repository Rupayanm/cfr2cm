from collections import deque
import math
for _ in range(int(input())):
    n = int(input())
    ai = list(map(int, input().split()))
    ai.sort()
    ans = deque([])
    for i in range(math.ceil(n/2)):
        ans.appendleft(ai[-i-1])
        ans.appendleft(ai[i])
    if n%2:
        ans.popleft()
    print(*ans)