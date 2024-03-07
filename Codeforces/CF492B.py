""""于2023-8-31测试通过"""
str_input = input()
data_list = str_input.split()
n = int(data_list[0])
l = int(data_list[1])

str_input = input()
data_list = str_input.split()
for i in range(0, n):
    data_list[i] = int(data_list[i])

data_list.sort()
distance_list = []
for i in range(0, n):
    if i == 0:
        distance_list.append(data_list[0] * 2)
    else:
        distance_list.append(data_list[i] - data_list[i - 1])
    if i == n - 1:
        distance_list.append((l - data_list[-1]) * 2)

print(max(distance_list) / 2)