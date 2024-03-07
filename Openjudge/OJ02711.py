"""于2023-12-24测试通过"""
n = int(input())
ls = list(map(int, input().split()))
dp_left, dp_right = [1]*n, [1]*n
for i in range(1, n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if ls[j] < ls[i]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)
print(min([n - dp_left[i] - dp_right[i] + 1 for i in range(n)]))
