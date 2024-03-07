"""于2023-10-4测试通过"""
maps = [[None for j in range(1025)] for i in range(1025)]
d, n = int(input()), int(input())
max_num = 0
count = 0
for i in range(n):
    x, y, num = map(int, input().split())
    for j in range(max(x - d, 0), min(x + d + 1, 1025)):
        for k in range(max(y - d, 0), min(y + d + 1, 1025)):
            if maps[j][k]:
                maps[j][k] += num
            else:
                maps[j][k] = num
            if maps[j][k] > max_num:
                max_num = maps[j][k]
                count = 1
            elif maps[j][k] == max_num:
                count += 1

print(count, max_num)