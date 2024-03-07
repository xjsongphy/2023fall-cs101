"""于2023-12-28测试通过"""
def add(i, j):
    if i in dic:
        dic[i][j] = True
    else:
        dic[i] = {j: True}


for i in range(int(input())):
    n, m, k = map(int, input().split())
    print(f'Case {i + 1}:')
    dic = {}
    for _ in range(m):
        i, j = map(int, input().split())
        add(i, j)
        add(j, i)
    for _ in range(k):
        i, j = map(int, input().split())
        print(sum([k in dic[j] for k in dic[i]]))