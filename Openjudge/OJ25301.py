"""于2023-12-12测试通过"""
n = int(input())
dic = {}
for _ in range(n):
    n, m, d = map(str, input().split())
    t = (int(m), int(d))
    if t in dic:
        dic[t].append(n)
    else:
        dic[t] = [n]
for key in sorted(dic.keys()):
    if len(dic[key]) > 1:
        print(key[0], key[1], ' '.join(dic[key]))