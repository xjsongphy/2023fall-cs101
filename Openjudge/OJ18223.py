"""于2023-9-13测试通过"""


def main(i, nums, sum_num):
    if i == 4 and sum_num == 24:
        return True
    elif i == 4:
        return False

    sum_add = sum_num + nums[i]
    sum_sub = sum_num - nums[i]
    if main(i + 1, nums, sum_add) or main(i + 1, nums, sum_sub):
        return True
    else:
        return False


n = int(input())

for i in range(n):
    nums = [int(x) for x in input().split()]

    if main(0, nums, 0):
        print('YES')
    else:
        print('NO')
