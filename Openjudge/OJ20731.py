"""于2023-12-24测试通过"""
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
x, y = map(int, input().split())
x -= 1
y -= 1
if m <= 1 or n <= 1:
    print(sum([sum(i) for i in matrix]))
    exit()
t = sum(matrix[0]) + sum(matrix[-1]) + sum([matrix[i][0] + matrix[i][-1] for i in range(1, m - 1)])
if x == 0 and y != m - 1 and x != y:
    t = sum(matrix[y]) + sum(matrix[-1]) + sum([matrix[i][0] + matrix[i][-1] for i in range(m - 1)])
    t -= matrix[y][0] + matrix[y][-1]
elif x != 0 and y == m - 1 and x != y:
    t = sum(matrix[0]) + sum(matrix[x]) + sum([matrix[i][0] + matrix[i][-1] for i in range(1, m)])
    t -= matrix[x][0] + matrix[x][-1]
print(t)