"""于2023-9-11测试通过"""
n, k = map(int, input().split())
ls = [int(x) for x in input().split()]
two_seats = four_seats = 0
for i in range(k):
    while four_seats < n:
        if ls[i] >= 4:
            four_seats += 1
            ls[i] -= 4
        else:
            break
for i in range(k):
    if four_seats >= n:
        break
    if ls[i] == 3:
        ls[i] = 0
        four_seats += 1
ls.sort()
for i in range(k):
    if four_seats >= n:
        break
    if ls[i] == 1:
        found = False
        for j in range(i + 1, k):
            if ls[j] == 2:
                found = True
                break
        if found:
            ls[i] = 0
            ls[j] = 0
            four_seats += 1
        else:
            for j in range(i + 1, k):
                if ls[j] == 1:
                    found = True
                    break
            ls[i] = 0
            four_seats += 1
            ls[j] = [ls[j], 0][found]
for i in range(k):
    if four_seats >= n:
        break
    if ls[i] == 2:
        ls[i] = 0
        if n - four_seats >= 2 and ls.count(2) >= 3:
            ls[ls.index(2)] = 0
            ls[ls.index(2)] = 0
            four_seats += 2
        else:
            four_seats += 1
for i in range(k):
    two_seats += ls[i] // 2 + ls[i] % 2
if four_seats <= n and two_seats <= 2 * n:
    print('YES')
else:
    print('NO')