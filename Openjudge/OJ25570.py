""""于2023-12-6测试通过"""
n = int(input())
matrix = [list(map(int, input().split())) for _  in range(n)]
l = (n + 1)//2
print(max([sum(matrix[i][i:n - i]) + [sum(matrix[n - i - 1][i:n - i]), 0][n % 2 and i == l - 1]+ sum([matrix[j][i] + matrix[j][n - i - 1] for j in range(i + 1, n - i - 1)]) for i in range(l)]))