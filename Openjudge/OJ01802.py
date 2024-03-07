"""于2023-12-27测试通过"""
w = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
words = {i: 0 for i in w}

for _ in range(4):
    for s in input():
        if s in words:
            words[s] += 1
t = words.values()
h = max([i for i in t])
matrix = [[' ']*26 for _ in range(h)] + [list(w)]
idx = 0
for key, value in words.items():
    for i in range(value):
        matrix[h - 1 - i][idx] = '*'
    idx += 1
for i in matrix:
    print(' '.join(i).rstrip())