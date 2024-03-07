"""于2023-10-20测试通过"""
n = int(input())
h = list(map(int, input().split()))
right = v = index = 0
while index < n - 1:
    top = 0
    for i in range(index + 1, n):
        if h[i] > top:
            top, right = h[i], i
        if h[i] >= h[index]:
            top = h[index]
            break
    for i in range(index + 1, right):
        v += top - h[i]
    index = right
print(v)
