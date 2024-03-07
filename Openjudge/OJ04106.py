"""于2023-10-11测试通过"""
n = int(input())
for i in range(n):
    strings = {}
    for j in input():
        if strings.get(j):
            strings[j] += 1
        else:
            strings[j] = 1
    for j in strings.keys():
        if strings[j] == 2:
            print(j)
            break