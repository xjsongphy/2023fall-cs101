"""于2023-10-18测试通过"""
n, m1, m2 = map(int, input().split())
matrix1, matrix2 = {}, {}
for i in range(m1):
    data = tuple(map(int, input().split()))
    matrix1[data[:2]] = data[2]
for i in range(m2):
    data = tuple(map(int, input().split()))
    matrix2[data[:2]] = data[2]

for i in range(n):
    for j in range(n):
        value = 0
        for k in range(n):
            if (i, k) not in matrix1 or (k, j) not in matrix2:
                continue
            value += matrix1[(i, k)]*matrix2[(k, j)]
        if value != 0:
            print(i, j, value)