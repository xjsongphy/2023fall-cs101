"""于2023-10-18测试通过"""
n, w = map(int, input().split())
datas = {}
for i in range(n):
    data = list(map(int, input().split()))
    if data[0]/data[1] in datas:
        datas[data[0]/data[1]][0] += data[0]
        datas[data[0]/data[1]][1] += data[1]
    else:
        datas[data[0]/data[1]] = data
value = 0
for i in sorted(datas.keys(), reverse=True):
    value += [datas[i][0]*w/datas[i][1], datas[i][0]][w >= datas[i][1]]
    w -= datas[i][1]
    if w < 0:
        break
print('%.1f' % value)