"""于2023-11-21测试通过"""
n = int(input())
ls = list(map(int, input().split()))
count, i = 1, 0
try:
    while i < n - 1:
        j = i + 1
        count += 1
        if ls[i + 1] > ls[i]:
            while ls[j] >= ls[j - 1]:
                j += 1
        elif ls[i + 1] < ls[i]:
            while ls[j] <= ls[j - 1]:
                j += 1
        else:
            count -= 1
            j += 1
        i = j - 1
except:
    pass
print(count)