"""于2023-10-11测试通过"""
# n = int(input())
# nums = input().split()
# for i in range(n - 1):
#     for j in range(i+1, n):
#         if nums[i] + nums[j] < nums[j] + nums[i]:
#             nums[i], nums[j] = nums[j], nums[i]
# print(''.join(nums), end=' ')
# nums.reverse()
# print(''.join(nums))


def sorting(ls):
    length = len(ls)
    if length <= 1:
        return ls
    elif length == 2:
        if ls[0] + ls[1] < ls[1] + ls[0]:
            ls.reverse()
        return ls
    middle = ls[int(length/2)]
    l, r, mid_ls = [], [], []
    for i in ls:
        if i + middle > middle + i:
            l.append(i)
        elif i + middle < middle + i:
            r.append(i)
        else:
            mid_ls.append(i)
    return sorting(l) + mid_ls + sorting(r)


input()
ls = sorting(input().split())
print(''.join(ls), end=' ')
ls.reverse()
print(''.join(ls))
