""""""
n = int(input())
coins = sorted([int(i) for i in input().split()], reverse=True)
sums = [coins[0]]
for i in range(1, n):
    sums.append(sums[-1] + coins[i])

for i in range(n):
    if sums[i] > sums[-1] / 2:
        print(i + 1)
        break