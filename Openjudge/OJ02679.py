"""于2023-8-31测试通过"""
k = int(input())

sum = 0
for i in range(1, k + 1):
    sum += i**3

print(sum)