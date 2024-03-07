""""""
input()
ls = list(map(int, input().split()))
key = sorted(set(ls))
ans = 0
l = len(key)
num = {}
for i in ls:
    if num.get(i):
        num[i] += 1
    else:
        num[i] = 1
dp = None
i = 0
while i < l:
    if num.get(key[i] + 1):
        j = i + 1
        while j < l:
            if not num.get(key[j] + 1):
                j += 1
                break
            j += 1
        dp = [[0, 0] for _ in range(j - i + 1)]
        for k in range(1, j - i + 1):
            if k == 1:
                dp[k][0] = num[key[i + k - 1]]*key[i + k - 1]
                dp[k][1] = 0
            else:
                dp[k][0] = max(dp[k - 1][1], dp[k - 2][0]) + num[key[i + k - 1]]*key[i + k - 1]
                dp[k][1] = max(dp[k - 1][0], dp[k - 1][1])
        ans += max(dp[-1][0], dp[-1][1])
        i = j
    else:
        ans += num[key[i]]*key[i]
        i += 1
print(ans)