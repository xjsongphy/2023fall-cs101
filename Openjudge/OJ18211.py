"""于2023-12-25测试通过"""
p = int(input())
ls = sorted(list(map(int, input().split())))
total = 0
sell = 0
i, j = 0, len(ls) - 1
while True:
    if i == j and p >= ls[i]:
        total += 1
        break
    if p >= ls[i]:
        p -= ls[i]
        total += 1
        i += 1
    elif total > sell:
        if p + ls[j] >= ls[i]:
            p += ls[j]
            j -= 1
            sell += 1
        else:
            break
    else:
        break
print(total - sell)