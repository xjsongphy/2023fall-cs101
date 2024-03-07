"""于2023-12-7测试通过"""
m, n = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
primes = []
lim = 10**4
nums = {i + 1: 1 for i in range(1, 10**4)}
for i in range(2, 10**4 + 1):
    if nums[i]:
        primes.append(i)
    for j in primes:
        if i*j > lim:
            break
        nums[i*j] = 0
        if i % j == 0:
            break
t_primes = {i**2: 1 for i in primes}
for i in range(m):
    count = sum_score = 0
    for j in ls[i]:
        if j in t_primes:
            count += 1
            sum_score += j
    if count:
        print('%.2f' % (sum_score/len(ls[i])))
    else:
        print(0)