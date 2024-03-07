"""于2023-12-13测试通过"""
n = int(input())
color = {}
nums = {}
ans = 0
ls = list(map(int, input().split()))
first, second = 0, 0

for i in range(n):
    key = ls[i]
    if key in color:
        value = color[key]
        nums[value] -= 1
        if not nums[value]:
            del nums[value]
            if value == second and second + 1 == first:
                second = 0
                for j in nums:
                    if second < j < first:
                        second = j
        value += 1
        color[key] += 1
    else:
        value = color[key] = 1
    if value in nums:
        nums[value] += 1
    else:
        nums[value] = 1
        if value > first:
            if first in nums:
                second = first
            first = value
        elif value > second:
            second = value
    if second == 0 and nums[first] == 1:
        ans = i
    elif first == 1:
        ans = i
    elif first - second == nums[first] == 1 and len(nums) == 2:
        ans = i
    elif second == 1:
        if nums[second] == 1:
            ans = i
print(ans + 1)