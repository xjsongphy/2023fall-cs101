"""于2023-10-14测试通过"""
n = int(input())
ratings = [int(i) for i in input().split()]
candies = [0 for i in range(n)]
i = 0
while i < n:
    j = i + 1
    while j < n:
        if ratings[j] <= ratings[j - 1]:
            break
        candies[j - 1] = j - i
        if j == n - 1:
            candies[j] = j - i + 1
        j += 1
    i = j
i = 0
while i < n:
    j = i + 1
    while j < n:
        if ratings[n - 1 - j] <= ratings[n - j]:
            break
        candies[n - j] = j - i
        if j == n - 1:
            candies[n - 1 - j] = j - i + 1
        j += 1
    i = j
candies[0] = [candies[0], 1][candies[0] == 0]
candies[-1] = [candies[-1], 1][candies[-1] == 0]

for i in range(1, n - 1):
    if candies[i] == 0:
        candies[i] = 1 + [max(candies[i - 1], candies[i + 1]), 0][ratings[i] == ratings[i - 1] == ratings[i + 1]]
print(sum(candies))
