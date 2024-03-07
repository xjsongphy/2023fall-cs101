"""于2023-12-24测试通过"""
n, m = map(int, input().split())
ls = list(map(int, input().split()))
nums = {}
counts = {0: m}
ans = 1
min_count = 0

for i in range(n):
    if ls[i] not in nums:
        nums[ls[i]] = 1
        counts[0] -= 1
        if counts[0] == 0:
            nums = {}
            counts = {0: m}
            ans += 1
print(ans)
