"""于2023-10-5测试通过"""
s = int(input())
nums = {i: 1 for i in range(2, s)}

for num in nums.keys():
    i = 2
    while i*num < s:
        nums[i*num] = 0
        i += 1

begin = s // 2 + 1
while True:
    if nums[begin] == 1 and nums[s - begin] == 1:
        print(begin*(s - begin))
        break
    begin -= 1