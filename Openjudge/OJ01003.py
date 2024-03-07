""""于2023-8-25测试通过"""

input_list = []

while True:
    temp_vary = float(input())

    if temp_vary == 0.0:
        break
    else:
        input_list.append(temp_vary)

for single_vary in input_list:
    sigma = 0.0
    i = 0

    while sigma < single_vary:
        sigma = sigma + 1 /(i + 2)
        i += 1
    print(str(i) + ' card(s)')