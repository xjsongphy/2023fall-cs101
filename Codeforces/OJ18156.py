"""于2023-12-1测试通过"""
from bisect import bisect_left as bl
n = int(input())/2
upper, lower = [], []
for i in input().split():
    i = int(i)
    if i >= n:
        upper.append(i - n)
    else:
        lower.append(i - n)
upper.sort()
lower.sort(reverse=True)
ans = {}
j = 0
u = len(upper)
for i in lower:
    j = bl(upper, -i)
    if j < u:
        t = upper[j] + i
        key = abs(t)
        if key in ans:
            ans[key] = min(t, ans[key])
        else:
            ans[key] = t
    if j - 1 >= 0:
        t = upper[j - 1] + i
        key = abs(t)
        if key in ans:
            ans[key] = min(t, ans[key])
        else:
            ans[key] = t
if u >= 2:
    t = upper[0] + upper[1]
    ans[t] = t
if len(lower) >= 2:
    t = lower[0] + lower[1]
    ans[-t] = t
print(int(ans[min(ans.keys())] + 2*n))
