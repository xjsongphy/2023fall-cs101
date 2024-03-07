"""于2023-11-29测试通过  """
from copy import deepcopy
s = None
ans = []


def func(i, matrix, ls):
    global ans
    for j in range(8):
        if not matrix[i][j]:
            new_ls = [k + str(j + 1) for k in ls]
            if i == 7:
                ans += new_ls
                continue
            new_matrix = deepcopy(matrix)
            for k in range(i, 8):
                new_matrix[k][j] = 8
            for k in range(i + 1, 8):
                if j + k - i < 8:
                    new_matrix[k][j + k - i] = 1
            for k in range(i + 1, 8):
                if 0 <= j - k + i:
                    new_matrix[k][j - k + i] = 1
            func(i + 1, new_matrix, new_ls)


func(0, [[0]*8 for _ in range(8)], [''])
ans.sort()
print(' '.join(ans))
output = ''
for _ in range(int(input())):
    output += ans[int(input()) - 1] + '\n'
print(output)

# 打表解法
# ans = '15863724 16837425 17468253 17582463 24683175 25713864 25741863 26174835 26831475 27368514 27581463 28613574 31758246 35281746 35286471 35714286 35841726 36258174 36271485 36275184 36418572 36428571 36814752 36815724 36824175 37285146 37286415 38471625 41582736 41586372 42586137 42736815 42736851 42751863 42857136 42861357 46152837 46827135 46831752 47185263 47382516 47526138 47531682 48136275 48157263 48531726 51468273 51842736 51863724 52468317 52473861 52617483 52814736 53168247 53172864 53847162 57138642 57142863 57248136 57263148 57263184 57413862 58413627 58417263 61528374 62713584 62714853 63175824 63184275 63185247 63571428 63581427 63724815 63728514 63741825 64158273 64285713 64713528 64718253 68241753 71386425 72418536 72631485 73168524 73825164 74258136 74286135 75316824 82417536 82531746 83162574 84136275'.split()
# output = ''
# for _ in range(int(input())):
#     output += ans[int(input()) - 1] + '\n'
# print(output)