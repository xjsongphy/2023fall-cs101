"""于2023-12-8测试通过"""
for _ in range(int(input())):
    n = int(input())
    dic = {}
    for i in map(int, input().split()):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    if 0 not in dic:
        print(0)
        continue
    dp = [0, dic[0]]
    is_min = [(dic[0], 0)]
    min_num = dic[0]
    i = 1
    while i in dic:
        if dic[i] < min_num:
            is_min.append((dic[i], i))
            min_num = dic[i]
        i += 1
    i = 1
    while i in dic:
        ls = []
        for a, b in is_min:
            if b > i:
                break
            ls.append(a*(i + 1) + b + dp[b])
        dp.append(min(ls))
        i += 1
    print(dp[-1])