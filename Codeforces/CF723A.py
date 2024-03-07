"""于2023-8-31测试通过"""
str_input = input()
data_list = str_input.split()

x_list = []
for data in data_list:
    x_list.append(int(data))

x_list.sort()
print(x_list[-1] - x_list[0])