"""于2023-12-24测试通过"""
s, e = input().split()
ls = input().split()
l = len(ls)
visited = [0]*l
if len(s) != len(e) or len(s) != len(ls[0]):
    print(0)


def diff(s, e):
    return sum([(s[i] != e[i]) for i in range(len(s))]) == 1


def dfs(s, visited):
    if diff(s, e):
        return 1
    ans = []
    for i in range(l):
        if visited[i]:
            continue
        if diff(s, ls[i]):
            new_visited = visited[:]
            new_visited[i] = 1
            t = dfs(ls[i], new_visited)
            if t != -1:
                ans.append(1 + t)
    return min(ans) if ans else -1


print(dfs(s, visited) + 1)