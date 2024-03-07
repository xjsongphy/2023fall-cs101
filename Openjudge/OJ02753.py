""""于2023-8-26测试通过"""
max = 1

total = int(input())
input_list = []

for i in range(0, total):
    input_list.append(int(input()))
    if input_list[-1] > max:
        max = input_list[-1]

num_list = [1, 1]
if max > 2:
    for i in range(0, max - 2):
        num_list.append(num_list[-1] + num_list[-2])

for input_num in input_list:
    print(num_list[input_num - 1])