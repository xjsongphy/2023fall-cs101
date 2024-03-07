"""于2023-11-27测试通过"""
n, x, y = map(int, input().split())
d = {}
for _ in range(n):
    t = input().split()
    if d.get(t[1]):
        d[t[1]][1] += int(t[2])
        d[t[1]][0] += 1
    else:
        d[t[1]] = [1, int(t[2])]
for key, value in d.items():
    d[key] = (value[0] >= x and value[1]/value[0] > y)
for _ in range(int(input())):
    print(['no', 'yes'][d[input()]])