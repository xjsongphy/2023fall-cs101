"""于2023-10-18测试通过"""
n, k = map(int, input().split())
nums = list(map(int, input().split()))
part = nums[:k]
pre_max = max(part)
for i in range(k, n):
    print(pre_max, end=' ')
    if nums[i] > pre_max:
        pre_max = nums[i]
        part[i % k] = nums[i]
    elif part[i % k] == pre_max:
        part[i % k] = nums[i]
        pre_max = max(part)
    else:
        part[i % k] = nums[i]
print(pre_max)
