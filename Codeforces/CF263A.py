"""于2023-9-6测试通过"""
index = None

for i in range(5):          #读取输入，找到1的位置
    input_list = input().split()
    for j in range(5):
        if input_list[j] == '1':
            index = (i, j)
            break

print(abs(index[0] - 2) + abs(index[1] - 2))