"""于2023-9-10测试通过"""
input_list = input().split()
l = int(input_list[0])
m = int(input_list[1])

axis = [0 for i in range(l + 1)]

for i in range(m):
    input_list = input().split()
    a = int(input_list[0])
    b = int(input_list[1])

    for j in range(a, b + 1):
        axis[j] = 1

print(axis.count(0))