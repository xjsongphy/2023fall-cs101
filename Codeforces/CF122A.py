"""于2023-10-13测试通过"""
from math import sqrt


n = int(input())
sqrt_n = int(sqrt(n)) + 2
found = False
for i in range(1, sqrt_n):
    if n % i == 0:
        for j in str(i):
            if j != '4' and j != '7':
                found = False
                break
            found = True
        if found:
            print('YES')
            exit()
        for j in str(n // i):
            if j != '4' and j != '7':
                found = False
                break
            found = True
        if found:
            print('YES')
            exit()
print('NO')