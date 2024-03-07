"""于2023-9-6测试通过"""
total = int(input())
input_list = list(input())
wanted_list = []

i = 0
while i < total:
    wanted_list.append(input_list[i])
    while i < total:
        if input_list[i] == wanted_list[-1]:
            i += 1
        else:
            break

print(total - len(wanted_list))