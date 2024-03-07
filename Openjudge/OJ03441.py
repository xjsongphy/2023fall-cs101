"""于2023-12-23测试通过"""
a_ls, b_ls, c_ls, d_ls = [], [], [], []
total = 0
n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split())
    a_ls.append(a)
    b_ls.append(b)
    c_ls.append(c)
    d_ls.append(d)

ab = {}
for a in a_ls:
    for b in b_ls:
        t = a + b
        if t in ab:
            ab[t] += 1
        else:
            ab[t] = 1

for c in c_ls:
    for d in d_ls:
        t = c + d
        if -t in ab:
            total += ab[-t]
print(total)