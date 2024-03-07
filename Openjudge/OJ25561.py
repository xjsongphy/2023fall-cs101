"""于2023-9-12测试通过"""
n, m = map(int, input().split())
prices = {}
coupons = {}
for i in range(n):
    datas = input().split()
    prices[i] = {}
    for data in datas:
        data = data.split(':')
        prices[i][int(data[0]) - 1] = int(data[1])
for i in range(m):
    datas = input().split()
    coupons[i] = {}
    for data in datas:
        data = data.split('-')
        coupons[i][int(data[0])] = int(data[1])
final = set()


def func(i, shops):
    if i == n:
        total = sum(shops)
        total -= (total//300)*50
        for j in range(m):
            sub = {0}
            for key, value in coupons[j].items():
                if shops[j] >= key:
                    sub.add(value)
            total -= max(sub)
        final.add(total)
        return
    for key, value in prices[i].items():
        t = shops[:]
        t[key] += value
        func(i + 1, t)


func(0, [0]*m)
print(min(final))
