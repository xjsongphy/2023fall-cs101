""""""
outputs = []
for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    ls = [(a[i], b[i]) for i in range(n)] + [(0, 0)]
    ls.sort(key=lambda t: t[0], reverse=True)
    dp = [ls[0][0]]
    b_sum = 0
    has_ans = False
    for i in range(n):
        b_sum += ls[i][1]
        dp.append(max(b_sum, ls[i + 1][0]))
        if dp[-1] > dp[-2]:
            outputs.append(dp[-2])
            has_ans = True
            break
    if not has_ans:
        outputs.append(dp[-1])
for ans in outputs:
    print(ans)