"""于2023-11-30测试通过"""
n = int(input())
ls = sorted([input() for _ in range(n)])
a, b = ls[n//2 - 1], ls[n//2]
ans = ''
la, lb = len(a), len(b)
for i in range(la):
    t = a[i]
    if i >= lb:
        if a[i] < 'Z':
            ans += [t, chr(ord(t) + 1)][i < la - 1]
            break
        ans += t
    elif ord(b[i]) - ord(t) >= 1:
        if i < la - 1 and i < lb - 1:
            ans += chr(ord(t) + 1)
            break
        else:
            ans += t
    else:
        ans += t
print(ans)