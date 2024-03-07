"""于2023-10-5测试通过"""
n = int(input())
sums = []

for a1 in range(n + 1):
    for a2 in range(n + 1):
        for a3 in range(n, -1, -1):
            if (a1 + a2) % 2 == (a2 + a3) % 3 == (a1 + a2 + a3) % 5 == 0:
                sums.append(a1 + a2 + a3)
                break

print(max(sums))