"""于2023-11-9测试通过"""
n = int(input())
nums = list(map(int, input().split()))
count = 0
l_sum = total = 0
all_sum = sum(nums)
for i in range(n):
    l_sum += nums[i]
    if 0 < i < n - 1 and l_sum == all_sum * 2 / 3:
        total += count
    if l_sum == all_sum/3:
        count += 1
print(total)
