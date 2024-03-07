"""于2023-11-21测试通过"""
n, m = map(int, input().split())
ls = [0] + list(map(int, input().split())) + [m]
on = off = 0
add = [0]
if n % 2:
    for i in range(n // 2 + 1):
        on += ls[2*i + 1] - ls[2*i]
        off += ls[2*i + 2] - ls[2*i + 1]
else:
    on = ls[1]
    for i in range(n // 2):
        on += ls[2*i + 3] - ls[2*i + 2]
        off += ls[2*i + 2] - ls[2*i + 1]
raw_on = on
for i in range(n // 2 + n % 2):
    on -= ls[2*i + 1] - ls[2*i]
    if ls[2*i + 2] - ls[2*i + 1] > 1:
        add.append(off - on - 1)
    off -= ls[2*i + 2] - ls[2*i + 1]
print(raw_on + max(add))