"""于2023-11-1测试通过"""
r1, c1 = map(int, input().split())
m1 = [list(map(int, input().split())) for _ in range(r1)]
r2, c2 = map(int, input().split())
m2 = [list(map(int, input().split())) for _ in range(r2)]
r3, c3 = map(int, input().split())
m3 = [list(map(int, input().split())) for _ in range(r3)]
if c1 != r2 or r1 != r3 or c2 != c3:
    print('Error!')
    exit()

for i in range(r3):
    for j in range(c3):
        for k in range(c1):
            m3[i][j] += m1[i][k]*m2[k][j]
    print(' '.join([str(s) for s in m3[i]]))