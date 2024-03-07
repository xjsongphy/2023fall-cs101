"""于2023-10-23测试通过"""
n = int(input())
for i in range(n):
    num = int(input())
    total = 0
    double = [True, False][num % 2]
    while True:
        if num == 4:
            total += 3
            break
        if num == 1:
            total += 1
            break
        if double:
            total += [1, num // 2][(num // 2) % 2]
            num = [num - 1, num // 2][(num // 2) % 2]
            double = False
        else:
            num -= 1
            total += 1
            double = True

        if num == 4:
            total += 1
            break
        if num == 1:
            break
        if double:
            num = [num - 1, num // 2][(num // 2) % 2]
            double = False
        else:
            num -= 1
            double = True
    print(total)