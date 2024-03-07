'''2023-8-26注：递归算法时间复杂度过大，此题应使用动态规划算法求解'''
import time


input_list = {}
deep = 0
max_sum = 0

def main_calculate(x_value, y_value, pre_sum):
    global max_sum
    if y_value == deep:
        sum = pre_sum + input_list[y_value][x_value]
        print(x_value)
        if sum > max_sum:
            max_sum = sum
    else:
        main_calculate(x_value, y_value + 1, pre_sum + input_list[y_value][x_value])
        main_calculate(x_value + 1, y_value + 1, pre_sum + input_list[y_value][x_value])


deep = int(input()) - 1
time_start = time.time()
for i in range(0, deep + 1):
    temp_str = input()
    temp_list = temp_str.split(' ')
    input_list[i] = []
    for j in range (0, i + 1):
        input_list[i].append(int(temp_list[j]))

main_calculate(0, 0, 0)
print(max_sum)
time_end = time.time()
print(time_end - time_start)

# deep = int(input()) - 1
# for i in range(0, deep + 1):
#     out_put = '1'
#     if i != 0:
#         for j in range(0, i):
#             out_put = out_put + ' ' + str(j + 1)
#
#     print(out_put)
