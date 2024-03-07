"""于2023-12-20测试通过"""
n, k = map(int, input().split())
data = {}
ls = list(map(int, input().split()))
for i in range(n):
    key, value = ls[2 * i], ls[2 * i + 1]
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
s = {int(i): 0 for i in input().split()}
others = {i: 0 for i in range(1, 314160)}
min_s = max_others = count = 0
num = {i: 0 for i in range(1, n + 1)}
num[0] = k
start = -1
keys = sorted(list(data.keys()))
if k == 314159:
    print(keys[-1])
    exit()
for t in keys:
    for c in data[t]:
        if c in s:
            p = s[c]
            num[p] -= 1
            if not num[p] and p == min_s:
                min_s += 1
            s[c] += 1
            num[p + 1] += 1
        else:
            others[c] += 1
            max_others = max(max_others, others[c])
    if max_others < min_s:
        if start == -1:
            start = t
    elif start != -1:
        count += t - start
        start = -1
print(count + [keys[-1] - start, 0][start == -1])