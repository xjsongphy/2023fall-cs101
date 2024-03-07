""""于2023-8-26测试通过"""
output_list = []

while True:
    input_str = input()
    if input_str == '0 0':
        break

    str_list = input_str.split()
    n = int(str_list[0])
    m = int(str_list[1])

    monkey_list = [x for x in range(1, n + 1)]
    i = 1
    j = 0
    while len(monkey_list) > 1:
        if i == m:
            i = 0
            monkey_list.pop(j)
            if j > len(monkey_list) - 1:
                j = 0
        else:
            if j == len(monkey_list) - 1:
                j = 0
            else:
                j += 1

        i += 1

    output_list.append(monkey_list[0])

for num in output_list:
    print(num)