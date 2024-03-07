""""于2023-8-31测试通过"""
x, y, z = 0, 0, 0

n = int(input())
for i in range(0, n):
    datas = [int(i) for i in input().split()]
    x += datas[0]
    y += datas[1]
    z += datas[2]

if x == y == z == 0:
    print('YES')
else:
    print('NO')
