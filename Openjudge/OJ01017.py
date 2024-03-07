"""于2023-9-27测试通过"""
while True:
    nums = [int(i) for i in input().split()]
    if sum(nums) == 0:
        break
    total = sum(nums[3:]) + nums[2]//4 + [1, 0][nums[2]%4 == 0]
    left_2 = 5*nums[3] + [0, 5, 3, 1][nums[2]%4]
    left_1 = 11*nums[4] + 20*nums[3] + [36 - 9*(nums[2]%4), 0][nums[2]%4 == 0]
    if left_2 >= nums[1]:
        left_2 -= nums[1]
        left_1 -= 4*nums[1]
    else:
        nums[1] -= left_2
        left_1 -= 4*left_2
        total += nums[1]//9 + [1, 0][nums[1]%9 == 0]
        left_1 += [36 - 4*(nums[1]%9), 0][nums[1]%9 == 0]
    if left_1 < nums[0]:
        nums[0] -= left_1
        total += nums[0]//36 + [1, 0][nums[0]%36 == 0]
    print(total)