"""于2023-9-17测试通过"""
from math import sqrt
a = int(input())
x = int(sqrt(a**2 + 1))
y = a**2 + 1

i = x
while True:
    if y % i == 0:
        x1 = y/i
        break
    i -= 1
x2 = i

ans1 = int(2*a + x1 + (a**2 + 1)/x1)
ans2 = int(2*a + x2 + (a**2 + 1)/x2)
print(min(ans1, ans2))

