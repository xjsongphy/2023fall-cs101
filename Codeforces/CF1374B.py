"""于2023-10-13测试通过"""
t = int(input())
for i in range(t):
    n = int(input())
    step = 0
    while n > 5:
        if n % 6 == 0:
            n = n // 6
            step += 1
        else:
            break
    while n > 2:
        if n % 3 == 0:
            n = n // 3
            step += 2
        else:
            break
    print([-1, step][n == 1])