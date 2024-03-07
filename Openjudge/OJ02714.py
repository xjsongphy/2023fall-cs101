""""于2023-8-26测试通过"""

total = int(input())
sum = 0.0

for i in range(0, total):
    sum += float(input())

print('%.2f'%(sum / total))