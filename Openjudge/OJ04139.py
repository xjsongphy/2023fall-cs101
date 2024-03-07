"""于2023-10-15测试通过"""
a, b, c = map(int, input().split())
print(sum([not (c - a*i) % b for i in range(c // a + 1)]))