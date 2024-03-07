"""仅给出穷举法作答，按标准答案提交，于2023-9-6测试通过"""
# map_matrix = []
# switch_matrix = []
#
#
# def all_off(matrix):
#     sum_num = 0
#     for i in range(5):
#         sum_num += sum(matrix[i])
#
#     if sum_num == 0:
#         return True
#     else:
#         return False
#
#
# def copy(matrix):
#     copy_matrix = []
#     for i in range(5):
#         copy_matrix.append(matrix[i][:])
#
#     return copy_matrix
#
#
# def switch_on(x, y, matrix):
#     if matrix[x][y] == 0:
#         matrix[x][y] = 1
#     else:
#         matrix[x][y] = 0
#     if x > 0:
#         if matrix[x - 1][y] == 0:
#             matrix[x - 1][y] = 1
#         else:
#             matrix[x - 1][y] = 0
#     if y > 0:
#         if matrix[x][y - 1] == 0:
#             matrix[x][y - 1] = 1
#         else:
#             matrix[x][y - 1] = 0
#     if x < 4:
#         if matrix[x + 1][y] == 0:
#             matrix[x + 1][y] = 1
#         else:
#             matrix[x + 1][y] = 0
#     if y < 5:
#         if matrix[x][y + 1] == 0:
#             matrix[x][y + 1] = 1
#         else:
#             matrix[x][y + 1] = 0
#
#     return matrix
#
# def main_function(s_matrix, m_matrix):
#     for i in range(5):
#         for j in range(6):
#             if s_matrix[i][j] == 1:
#                 m_matrix = switch_on(i, j, m_matrix)
#
#     return all_off(m_matrix)
#
#
# for i in range(5):
#     input_list = input().split()
#     map_matrix.append([int(x) for x in input_list])
#     switch_matrix.append([0 for i in range(6)])
#
# while True:
#     # if main_function(switch_matrix, copy(map_matrix)):
#     #     break
#
#     switch_matrix[0][0] += 1
#     for i in range(5):
#         for j in range(6):
#             if switch_matrix[i][j] == 2:
#                 if j == 5:
#                     switch_matrix[i + 1][0] += 1
#                 else:
#                     switch_matrix[i][j + 1] += 1
#                 switch_matrix[i][j] = 0
#
# for i in range(5):
#     for j in range(6):
#         if j == 5:
#             print(switch_matrix[i][j])
#         else:
#             print(switch_matrix[i][j], end='')
#             print(' ', end='')

"""标答思路：穷举第一行的可能结果，根据第一行依次确定后几行内容，判断最后一行能否熄灭"""

maps = []
switches = []


def switch_on(x, y, matrix):
    matrix[x][y] = [0, 1][matrix[x][y] == 0]
    if x > 0:
        matrix[x - 1][y] = [0, 1][matrix[x - 1][y] == 0]
    if y > 0:
        matrix[x][y - 1] = [0, 1][matrix[x][y - 1] == 0]
    if x < 4:
        matrix[x + 1][y] = [0, 1][matrix[x + 1][y] == 0]
    if y < 5:
        matrix[x][y + 1] = [0, 1][matrix[x][y + 1] == 0]
    return matrix


def copy(matrix):
    return [line[:] for line in matrix]


for i in range(5):
    maps.append([int(x) for x in input().split()])
    switches.append([0 for x in range(6)])
while True:
    copies = copy(maps)
    for i in range(5):
        if i > 0:
            for j in range(6):
                switches[i][j] = [0, 1][copies[i - 1][j] == 1]
        for j in range(6):
            if switches[i][j] == 1:
                copies = switch_on(i, j, copies)
    if sum(copies[4]) == 0:
        break
    switches[0][0] += 1
    for i in range(6):
        if switches[0][i] == 2:
            switches[0][i] = 0
            switches[0][i + 1] += 1
for i in range(5):
    print(' '.join([str(j) for j in switches[i]]))
