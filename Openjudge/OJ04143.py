"""于2023-11-6测试通过"""
n = int(input())
nums = sorted(list(map(int, input().split())))
nums_dict = {i: 0 for i in nums}
for num in nums:
    nums_dict[num] += 1
m = int(input())
for num in nums:
    if num > m // 2 + 1:
        break
    if nums_dict.get(m - num):
        if 2*num - m:
            print(num, m - num)
            exit()
        elif nums_dict[num] > 1:
            print(num, num)
            exit()
print('No')
