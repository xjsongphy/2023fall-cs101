"""于2023-12-13测试通过"""
from copy import copy
m, n = map(int, input().split())
nodes = {}
level = {}
ways = {i: {} for i in range(n)}

l_king = 0
for i in range(n):
    p, l, x = map(int, input().split())
    if not i:
        l_king = l
    elif abs(l - l_king) > m:
        for _ in range(x):
            input()
        continue
    level[i] = l
    nodes[i] = p
    for _ in range(x):
        t, v = map(int, input().split())
        ways[t - 1][i] = v
raw_nodes = copy(nodes)
min_levels = sorted(set([level[i] for i in nodes]))
min_ps = []
for min_level in min_levels:
    if min_level > l_king:
        break
    nodes = copy(raw_nodes)
    ls = list(nodes.keys())
    for i in ls:
        if level[i] < min_level or level[i] > min_level + m:
            del nodes[i]
    while True:
        min_p, index = nodes[0], 0
        for i in nodes:
            if nodes[i] < min_p:
                min_p = nodes[i]
                index = i
        if not index:
            min_ps.append(min_p)
            break
        del nodes[index]
        for key, value in ways[index].items():
            if key in nodes:
                nodes[key] = min(nodes[key], min_p + value)
print(min(min_ps))