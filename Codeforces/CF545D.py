"""于2023-10-25测试通过"""
n = int(input())
t = sorted(list(map(int, input().split())))
total_time, total = 0, 0
i, j = 0, -1
for i in range(n):
    while j < n - 1:
        j += 1
        if t[j] >= total_time:
            total += 1
            break
    total_time += t[j]
print(total)