"""于2023-10-25测试通过"""
n, m = map(int, input().split())
nums = list(map(int, input().split()))
indexes = [int(input()) - 1 for i in range(m)]
min_index = min(indexes)
distinct_nums, outputs = {}, [0]
i = n - 1
while i >= min_index:
    if distinct_nums.get(nums[i]):
        outputs.append(outputs[-1])
    else:
        distinct_nums[nums[i]] = 1
        outputs.append(outputs[-1] + 1)
    i -= 1
outputs.reverse()
for i in indexes:
    print(outputs[i - min_index])
