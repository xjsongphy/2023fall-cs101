"""于2023-10-11测试通过"""
m = int(input())

for i in range(m):
    n = int(input())
    fruits = {}
    for j in range(n):
        num, a, b = map(int, input().split())
        fruits[a + b] = (num, a, b)
    values = sorted(fruits.keys())
    fruit = fruits[values[-2]]
    print(fruit[0], fruit[1], fruit[2], values[-2])