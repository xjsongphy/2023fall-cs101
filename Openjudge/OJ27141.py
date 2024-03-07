""""""
n = int(input())
dp = list(map(int, input().split()))
dp[0] -= 520
dic = {dp[0]: [0]}


def add(i, j):
    if i in dic:
        dic[i].append(j)
    else:
        dic[i] = [j]


add(0, -1)
for i in range(1, n):
    dp[i] += dp[i - 1] - 520
    add(dp[i], i)
print(max([max(ls) - min(ls) for ls in dic.values()])*520)