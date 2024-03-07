"""于2023-10-25测试通过"""
n = int(input())
total = 0
not_full = [0, 0, 0]
for s in list(map(int, input().split())):
    if s == 4:
        total += 1
    elif not_full[3 - s] > 0:
        not_full[3 - s] -= 1
    else:
        not_full[s - 1] += 1
        total += 1
if not_full[0] // 2 >= not_full[1]:
    total -= not_full[1]*2
    not_full[0] -= not_full[1]*2
    total -= not_full[0] - not_full[0] // 4 - (not_full[0] % 4 != 0)
else:
    total -= not_full[0]
print(total)