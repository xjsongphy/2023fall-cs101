"""于2023-12-23测试通过"""
dic = {}
while True:
    t = input().split()
    if t:
        value, key = t
        dic[t[1]] = t[0]
    else:
        break
while True:
    try:
        key = input()
    except EOFError:
        break
    t = dic.get(key)
    print(t if t else 'eh')