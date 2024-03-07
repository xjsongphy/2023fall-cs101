""""于2023-8-31测试通过"""
str_input = input()
data_list = str_input.split()
m = int(data_list[0])
n = int(data_list[1])

if n % 2 == 0:
    total = m * n / 2
else:
    total = (n // 2) * m
    total += m // 2

print(int(total))