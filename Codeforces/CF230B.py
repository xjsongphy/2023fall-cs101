"""于2023-10-11测试通过"""
input()
datas = [int(i) for i in input().split()]
inputs = {i: 1 for i in datas}

max_sqrt = 1000000
nums = {i: 1 for i in range(2, max_sqrt + 1)}
primes = []

for i in range(2, max_sqrt + 1):
    if nums[i]:
        primes.append(i)
        if inputs.get(i**2):
            inputs[i**2] = 0
    for j in primes:
        if i*j > max_sqrt:
            break
        nums[i*j] = 0
        if i % j == 0:
            break
for i in datas:
    print(['YES', 'NO'][inputs[i]])
