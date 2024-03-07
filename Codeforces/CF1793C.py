"""于2023-10-26测试通过"""
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    i, j = 0, n - 1
    min_max = [1, n]
    no_ans = True
    while i + 2 < j:
        if nums[i] in min_max or nums[j] in min_max:
            for k in range(2):
                if min_max[k] == nums[i]:
                    i += 1
                    min_max[k] += [1, -1][k]
                elif min_max[k] == nums[j]:
                    j -= 1
                    min_max[k] += [1, -1][k]
            continue
        if i + 2 < j:
            print(i + 1, j + 1)
            no_ans = False
        break
    if no_ans:
        print(-1)