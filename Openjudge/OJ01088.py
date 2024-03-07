"""于2023-11-24测试通过"""
from queue import LifoQueue

r, c = map(int, input().split())
m = [[10001]*(c + 2)]
m += [[10001] + list(map(int, input().split())) + [10001] for _ in range(r)]
m += [[10001]*(c + 2)]

searched = {}
dp = {}
for i in range(1, r + 1):
    for j in range(1, c + 1):
        ls = LifoQueue()
        if searched.get((i, j)):
            continue
        max_l = []
        ls.put((i, j, 1))
        while not ls.empty():
            loc = ls.get()
            x, y, l = loc[0], loc[1], loc[2]
            searched[(x, y)] = 1
            h = m[x][y]
            try:
                max_l.append(l + dp[(x, y)] - 1)
            except:
                if m[x - 1][y] < h:
                    ls.put((x - 1, y, l + 1))
                if m[x + 1][y] < h:
                    ls.put((x + 1, y, l + 1))
                if m[x][y - 1] < h:
                    ls.put((x, y - 1, l + 1))
                if m[x][y + 1] < h:
                    ls.put((x, y + 1, l + 1))
                max_l.append(l)
        dp[(i, j)] = max(max_l)
print(max(dp.values()))

# # DFS解法，耗时更短
# def longestSlidePath(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     dp = [[0 for _ in range(cols)] for _ in range(rows)]  # 初始化DP矩阵，用来存储最长滑坡的长度
#
#     def dfs(i, j):  # 定义DFS函数来计算以(i, j)为起点的最长滑坡长度
#         if dp[i][j] > 0:  # 如果已经计算过，则直接返回该点的结果
#             return dp[i][j]
#         maxLen = 1  # 初始化最长滑坡长度为1
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
#         for dx, dy in directions:  # 遍历四个方向
#             x, y = i + dx, j + dy  # 计算下一个点的坐标
#             if 0 <= x < rows and 0 <= y < cols and matrix[x][y] < matrix[i][
#                 j]:  # 判断下一个点是否合法且满足高度要求
#                 maxLen = max(maxLen, 1 + dfs(x, y))  # 更新最长滑坡长度
#         dp[i][j] = maxLen  # 缓存结果
#         return maxLen
#
#     result = 0
#     for i in range(rows):
#         for j in range(cols):
#             result = max(result, dfs(i, j))  # 遍历每个点，更新最终结果
#     return result  # 返回最长滑坡长度
#
#
# # 示例用法
# r, c = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(r)]
# print(longestSlidePath(matrix))  # 输出最长滑坡长度
