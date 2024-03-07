"""于2023-11-2测试通过"""
i, j = None, None


def search():
    global i, j
    if j - i <= 1:
        print(ls[j] if ls[j] - num < num - ls[i] else ls[i])
        return
    mid = int((i + j)/2)
    if num > ls[mid]:
        i = mid
    else:
        j = mid
    search()


n = int(input())
ls = list(map(int, input().split()))
for _ in range(int(input())):
    i, j = 0, n - 1
    num = int(input())
    search()