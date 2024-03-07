"""于2023-12-24测试通过"""
n = int(input())
ls = []
count = 0
while len(ls) < n*n:
    ls += list(map(int, input().split()))
matrix = [[0]*n] + [[ls[j] for j in range(n)]] + [[] for _ in range(n - 1)]
for i in range(2, n + 1):
    for j in range(n):
        matrix[i].append(matrix[i - 1][j] + ls[(i - 1)*n + j])
ans = set()
for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp = [matrix[j][0] - matrix[i - 1][0]]
        for k in range(1, n):
            dp.append(max(0, dp[-1]) + matrix[j][k] - matrix[i - 1][k])
        ans.add(max(dp))
print(max(ans))