""""于2023-8-26测试通过"""

n = int(input())
ans = 1

for i in range(0, n):
    ans = ans * (i + 1)

print(ans)