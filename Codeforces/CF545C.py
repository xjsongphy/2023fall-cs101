"""于2023-10-20测试通过"""
n, total = int(input()), 1
trees = {}

for i in range(n):
    trees[i] = list(map(int, input().split())) + [0]
    if i == 0:
        trees[0][2] = 1
    elif i > 1:
        if trees[i - 1][0] - trees[i - 2][0] > [0, trees[i - 2][1]][trees[i - 2][2] == -1] + trees[i - 1][1]:
            trees[i - 1][2] = 1
            total += 1
        elif trees[i][0] - trees[i - 1][0] > trees[i - 1][1]:
            trees[i - 1][2] = -1
            total += 1
print(total + [1, 0][n == 1])
