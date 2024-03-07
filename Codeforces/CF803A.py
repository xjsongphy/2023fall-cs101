""""""
n, k = map(int, input().split())
if k > n**2:
    print(-1)
    exit()
matrix = [['0']*n for i in range(n)]
i, j = 0, 0
while k > 0:
    if i == j:
        matrix[i][j] = '1'
        k -= 1
    elif k > 1:
        matrix[i][j] = matrix[j][i] = '1'
        k -= 2
    else:
        if i == n - 1:
            print(-1)
            exit()
        matrix[i + 1][i + 1] = '1'
        k -= 1
    j += 1
    if j == n:
        i += 1
        j = i
for i in range(n):
    print(' '.join(matrix[i]))