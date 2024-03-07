"""于2023-9-26测试通过"""
a, b, k = map(int, input().split())
matrix = [[0 for j in range(b)] for i in range(a)]
for i in range(k):
    r, s, p, t = map(int, input().split())
    if not t:
        t = -100
    p = p // 2
    r -= 1
    s -= 1
    for j in range(max(r - p, 0), min(r + p + 1, a)):
        for k in range(max(s - p, 0), min(s + p + 1, b)):
            matrix[j][k] += t
max_num = -1
for i in range(a):
    max_num = max(max_num, max(matrix[i]))

if max_num < 0:
    print(0)
else:
    total = 0
    for i in range(a):
        total += matrix[i].count(max_num)
    print(total)
