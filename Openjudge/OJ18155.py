"""于2023-12-20测试通过"""
t = int(input())
nums = {}
for i in input().split():
    num = int(i)
    if num > t:
        continue
    keys = list(nums.keys())
    for j in keys:
        p = num * j
        if p > t or p in nums:
            continue
        nums[p] = 1
    if num in nums:
        continue
    nums[num] = 1
print(['NO', 'YES'][t in nums])