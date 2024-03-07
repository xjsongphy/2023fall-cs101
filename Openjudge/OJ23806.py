"""于2023-12-7测试通过"""
ls = map(int, input().split())
dic = {}
for i in ls:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
ls = sorted(dic.keys())
n = len(ls)
total = 0
for i in range(n):
    key_i = ls[i]
    if key_i > 0:
        break
    elif key_i == 0:
        total += (dic[key_i] >= 3)
        break
    if dic[key_i] >= 2:
        total += (-2*key_i in dic)
    for j in range(i + 1, n):
        key_j = ls[j]
        t = -key_i - key_j
        if t < key_j:
            break
        if t == key_j:
            total += (dic[t] > 1)
        else:
            total += (t in dic)
print(total)