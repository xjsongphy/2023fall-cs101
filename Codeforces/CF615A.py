"""于2023-9-6测试通过"""
input_list = [int(x) for x in input().split()]
n = input_list[0]
light_dict = {x: 0 for x in range(input_list[1])}

for i in range(n):
    input_list = [int(x) for x in input().split()]
    for j in input_list[1:]:
        light_dict[j - 1] = 1

if 0 in light_dict.values():
    print('NO')
else:
    print('YES')