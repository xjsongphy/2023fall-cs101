"""于2023-12-18测试通过"""
from queue import Queue

n, m = map(int, input().split())
way = {i: [] for i in range(n)}
for _ in range(m):
    u, v = map(int, input().split())
    way[u].append(v)
    way[v].append(u)

node, record = {}, {}
que = Queue()
loop = False
que.put(0)
i = count = 0

while len(node) < n:
    while i in node:
        i += 1
    que.put(i)
    while not que.empty():
        u = que.get()
        node[u] = 1
        for v in way[u]:
            if (u, v) in record or (v, u) in record:
                continue
            if v in node:
                loop = True
                record[(u, v)] = 1
                continue
            que.put(v)
            node[v] = record[(u, v)] = 1
    count += 1

t = ['no', 'yes']
print(f'connected:{t[count == 1]}')
print(f'loop:{t[int(loop)]}')