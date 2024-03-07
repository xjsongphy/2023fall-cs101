"""于2023-10-4测试通过"""
nums = [range(int(i) + 1) for i in input().split()]
weights = {}

for a1 in nums[0]:
    for a2 in nums[1]:
        for a3 in nums[2]:
            for a4 in nums[3]:
                for a5 in nums[4]:
                    for a6 in nums[5]:
                        weights[a1 + 2*a2 + 3*a3 + 5*a4 + 10*a5 + 20*a6] = None

print(f'Total={len(weights.keys()) - 1}')