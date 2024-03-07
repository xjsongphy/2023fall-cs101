"""于2023-11-29测试通过"""
def m():
    return map(int, input().split())


wx, wy = m()
bx, by = m()
vx, vy = m()
e = int(input())
hole = [(0, 0), (8, 0), (16, 0), (0, 5), (8, 5), (16, 5)]
t = [-1, 1]

if (bx, by) in hole:
    print(1)
    exit()

b = False
for _ in range(e + 1):
    if (wx, wy) == (bx, by):
        b = True
    if (wx, wy) in hole:
        print(-1)
        exit()
    if (bx, by) in hole:
        print(1)
        exit()
    if b:
        bx += vx
        by += vy
        vx *= t[0 < bx < 16]
        vy *= t[0 < by < 5]
    else:
        wx += vx
        wy += vy
        vx *= t[0 < wx < 16]
        vy *= t[0 < wy < 5]
print(0)