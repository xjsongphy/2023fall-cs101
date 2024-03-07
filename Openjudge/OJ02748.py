"""于2023-12-12测试通过"""
from itertools import permutations
s = list(input())
s = [''.join(i) for i in permutations(s)]
s.sort()
for i in s:
    print(i)