"""于2023-12-22测试通过"""
m, s, c = map(int, input().split())
ls = sorted([int(input()) for _ in range(c)])
print(ls[-1] - ls[0] + 1 + sum(sorted([ls[i] - ls[i + 1] + 1 for i in range(c - 1)])[:m - 1]))