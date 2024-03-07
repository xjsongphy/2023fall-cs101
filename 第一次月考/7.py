while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    circle = [i + 1 for i in range(n)]
    pre_index = -1
    index = 0
    for i in range(n - 1):
        index = (m % (n - i) + pre_index) % (n - i)
        pre_index = index - 1
        circle.pop(index)

    print(circle[0])