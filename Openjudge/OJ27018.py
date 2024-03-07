factorials = [1]
n = int(input())
for i in range(len(factorials), n + 1):
    factorials.append(factorials[-1]*i)
    factorials[-1] = factorials[-1] % 998244353
previous = list(map(int, input().split()))
num = 0
for i in range(n):
    for j in range(i + 1, n):
        if previous[j] < previous[i]:
            num += factorials[n - 1 - i]
    num = num % 998244353
print((num + 1) % 998244353)
print(factorials)