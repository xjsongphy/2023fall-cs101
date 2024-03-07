"""于2023-11-15测试通过"""
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(n - i):
        nums[-i - 1][j] += max(nums[-i][j], nums[-i][j + 1])
print(nums[0][0])