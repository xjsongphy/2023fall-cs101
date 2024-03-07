"""于2023-11-28测试通过"""
for _ in range(int(input())):
    txt, pat = map(str, input().split())
    n = len(txt)
    m = len(pat)
    ne = [0]*m
    for i in range(1, m):
        if pat[ne[i - 1] + 1] == pat[i] and ne[i - 1] + 1 < i:
            ne[i] = ne[i - 1] + 1
    ne = [0] + ne
    i = j = 0
    ans = []
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                ans.append(str(i - j))
                j = min(m - 1, ne[j] + 1)
        else:
            i += (not j)
            j = ne[j]
    if ans:
        print(' '.join(ans))
    else:
        print('no')
