""""于2023-8-26测试通过"""

num_8 = input()
num_10 = 0

for i in range(1, len(num_8) + 1):
    num_10 += int(num_8[-i]) * (8**(i - 1))

print(num_10)
