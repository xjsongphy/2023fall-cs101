"""于2023-8-31测试通过"""
n = int(input())

for i in range(0, n):
    str_input = input()
    if len(str_input) > 10:
        print(str_input[0] + str(len(str_input) - 2) + str_input[-1])
    else:
        print(str_input)