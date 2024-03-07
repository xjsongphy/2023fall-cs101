"""于2023-9-15测试通过"""
sum_money = 0.0

for i in range(12):
    sum_money += float(input())

print('$%.2f'%(sum_money / 12))