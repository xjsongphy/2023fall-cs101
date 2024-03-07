""""于2023-8-31测试通过"""
n = int(input())
str_input = input()
data_list = str_input.split()
sum = 0

for i in range(0, n):
    sum += int(data_list[i])

print(sum / n)