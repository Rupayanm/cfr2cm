def longestSemiRepetitiveSubstring( s: str) -> int:
    ans = 0
    ct = 0
    s+="#"
    right = 0
    for left in range(len(s)-1):
        while ct < 2 and right < len(s)-1:
            if s[right] == s[right - 1]:
                ct += 1
            if ct < 2:
                ans = max(ans, right - left + 1)
            right += 1
        if s[left] == s[left+1] :
            ct -= 1
    return ans



