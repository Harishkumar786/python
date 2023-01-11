def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    T = [[False] * (n + 1) for _ in range(m + 1)]
    T[0][0] = True
    for j in range(1, n + 1):
        if p[j-1] == '*':
            T[0][j] = T[0][j-2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                T[i][j] = T[i-1][j-1]
            elif p[j-1] == '*':
                T[i][j] = T[i][j-2] or T[i-1][j]
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    T[i][j] |= T[i-1][j]
    return T[m][n]

print(isMatch("aa","a"))
