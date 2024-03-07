"""于2023-10-5测试通过，2023-10-16优化算法"""
pairs = {}
max_num = 100**3
n = int(input())
nums = {i + 1: (i + 1)**3 for i in range(1, n)}
tri_sqrt = {(i + 1)**3: i + 1 for i in range(1, n)}
for i in range(2, n + 1):
    for j in range(i, n + 1):
        for k in range(j, n + 1):
            sum_num = nums[i] + nums[j] + nums[k]
            if tri_sqrt.get(sum_num):
                if pairs.get(tri_sqrt[sum_num]):
                    pairs[tri_sqrt[sum_num]].append((i, j, k))
                else:
                    pairs[tri_sqrt[sum_num]] = [(i, j, k)]
for i in sorted(pairs.keys()):
    for j in pairs[i]:
        print(f'Cube = {i}, Triple = ({j[0]},{j[1]},{j[2]})')