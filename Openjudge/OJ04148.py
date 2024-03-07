"""于2023-10-16测试通过"""
count = 1
while True:
    p, e, i, d = map(int, input().split())
    if d + p + e + i == -4:
        break
    p, e, i = p - d, e - d, i - d
    d = i % 33
    for j in range(0, 645):
        day = d + j*33
        if (day - p) % 23 == (day - e) % 28 == 0 and day > 0:
            print(f'Case {count}: the next triple peak occurs in {day} days.')
            break
    count += 1