"""于2023-12-4测试通过"""
n = int(input())
ls = list(map(float, input().split()))
min_price = ls[0]
for i in range(n):
    min_price = min(min_price, ls[i])
    ls[i] = 100 * ls[i] / min_price
print('%.2f' % max(ls))