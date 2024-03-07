"""于2023-10-15测试通过"""
nums = list(map(int, input().split()))
print(sum([[0, i][i < nums[0]] for i in nums[1:]]))