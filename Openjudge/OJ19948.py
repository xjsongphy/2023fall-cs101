n, m = map(int, input().split())
ranks = sorted(list(map(int, input().split())))
total = ranks[-1] - ranks[0]
for i in range(n - 1):
    ranks[i] -= ranks[i + 1]
ranks[-1] = 0
print(total + sum(sorted(ranks)[:m - 1]))