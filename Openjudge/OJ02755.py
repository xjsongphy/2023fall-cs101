""""""
# total = 0
#
#
# def recursion(sum, i):
#     if i == n:
#         if sum == 40:
#             global total
#             total += 1
#     else:
#         recursion(sum + ls[i], i + 1)
#         recursion(sum, i + 1)
#
#
# n = int(input())
# ls = [int(input()) for _ in range(n)]
# recursion(0, 0)
# print(total)

n = int(input())
ls = [int(input()) for _ in range(n)]
sum_ls = [0]
for num in ls:
    sum_ls += [i + num for i in sum_ls]
print(sum_ls.count(40))