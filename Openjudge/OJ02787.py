"""于2023-10-15测试通过"""
from itertools import permutations as f


def calculate(a, b):
    if b == 0.0:
        return [a, 0]
    return [a + b, a - b, a*b, a/b]


while True:
    num = [float(i) for i in input().split()]
    if sum(num) == 0:
        break
    try:
        for nums in set(f(num)):
            for i in calculate(nums[2], nums[3]):
                for j in calculate(nums[1], i):
                    for k in calculate(nums[0], j):
                        if 23.99 <= k <= 24.01:
                            1/0
                for j in calculate(nums[0], nums[1]):
                    for k in calculate(i, j):
                        if 23.99 <= k <= 24.01:
                            1/0
            for i in calculate(nums[0], nums[1]):
                for j in calculate(i, nums[2]):
                    for k in calculate(j, nums[3]):
                        if 23.99 <= k <= 24.01:
                            1/0
        print('NO')
    except:
        print('YES')

# shortest code
# from itertools import permutations as f
# def calculate(a, b):
#     if b == 0.0:return [a, 0]
#     return [a + b, a - b, a*b, a/b]
# while True:
#     num = [float(i) for i in input().split()]
#     if sum(num) == 0:break
#     try:
#         for nums in set(f(num)):
#             for i in calculate(nums[2], nums[3]):
#                 for j in calculate(nums[1], i):
#                     for k in calculate(nums[0], j):
#                         if 23.99 <= k <= 24.01:1/0
#                 for j in calculate(nums[0], nums[1]):
#                     for k in calculate(i, j):
#                         if 23.99 <= k <= 24.01:1/0
#             for i in calculate(nums[0], nums[1]):
#                 for j in calculate(i, nums[2]):
#                     for k in calculate(j, nums[3]):
#                         if 23.99 <= k <= 24.01:1/0
#         print('NO')
#     except:print('YES')
