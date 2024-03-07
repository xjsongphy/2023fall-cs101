"""于2023-8-31测试通过"""
n = int(input())
total = 0

for i in range(0, n):
    num_list = input().split()

    sum_num = 0
    for j in range(0, 3):
        sum_num += int(num_list[j])

    if sum_num >= 2:
        total += 1

print(total)