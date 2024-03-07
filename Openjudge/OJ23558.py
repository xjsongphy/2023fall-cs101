"""于2023-12-4测试通过"""
n, m, l = map(int, input().split())
dic = {i: [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
for i in range(n):
    dic[i].sort()
s = int(input())
print(s, end='')
searched = {}


def dfs(i, d):
    if d == 0:
        return
    searched[i] = 1
    for j in dic[i]:
        if j in searched:
            continue
        print(f' {j}', end='')
        searched[j] = 1
        dfs(j, d - 1)


dfs(s, l)