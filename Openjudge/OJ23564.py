"""于2023-10-13测试通过"""
n = int(input())
if n == 1:
    print(1)
    exit()

nums = {i: 1 for i in range(2, n + 1)}
ls = []

total = 0
for i in range(2, n + 1):
    if nums[i]:
        ls.append(i)
        if n % i == 0:
            n = n // i
            total += 1
            if n % i == 0:
                print(0)
                exit()
        if i > n:
            break
    for j in ls:
        if i*j > n:
            break
        nums[i*j] = 0
        if i % j == 0:
            break
print([1, -1][total % 2])