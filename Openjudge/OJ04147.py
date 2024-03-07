"""于2023-11-30测试通过"""
def hanoi(n, a, b, c):
    if n == 1:
        print(f'{1}:{a}->{c}')
    else:
        hanoi(n - 1, a, c, b)
        print(f'{n}:{a}->{c}')
        hanoi(n - 1, b, a, c)


n, a, b, c = map(str, input().split())
n = int(n)
hanoi(n, a, b, c)