"""于2023-12-7测试通过"""
m = int(input())
ls = list(map(int, input().split()))
lim = 32
square = {i**2: 1 for i in range(1, lim)}
key = square.keys()
for i in ls:
    for j in key:
        if j >= i:
            break
        if i - j in square:
            print(bin(i), oct(i), hex(i))
            break
