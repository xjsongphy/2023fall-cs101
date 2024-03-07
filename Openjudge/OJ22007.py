"""于2023-12-13测试通过"""
from copy import deepcopy
s = None
ans = []
n = 0


def func(i, matrix, ls):
    global ans
    for j in range(n):
        if not matrix[i][j]:
            new_ls = [k + ' ' + str(j) for k in ls]
            if i == n - 1:
                ans += new_ls
                continue
            new_matrix = deepcopy(matrix)
            for k in range(i, n):
                new_matrix[k][j] = n
            for k in range(i + 1, n):
                if j + k - i < n:
                    new_matrix[k][j + k - i] = 1
            for k in range(i + 1, n):
                if 0 <= j - k + i:
                    new_matrix[k][j - k + i] = 1
            func(i + 1, new_matrix, new_ls)


n = int(input())
func(0, [[0]*n for _ in range(n)], [''])
ans.sort()
if ans:
    for i in ans:
        print(i.lstrip())
else:
    print("NO ANSWER")