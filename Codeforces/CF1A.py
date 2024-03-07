""""于2023-8-31测试通过"""
str_input = input()
data_list = str_input.split()
n = int(data_list[0])
m = int(data_list[1])
a = int(data_list[2])

if n % a == 0:
    n = n / a
else:
    n = int(n / a) + 1

if m % a == 0:
    m = m / a
else:
    m = int(m / a) + 1

print(int(m * n))