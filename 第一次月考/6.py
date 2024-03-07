n = int(input())
sums = []

for a1 in range(n + 1):
    for a2 in range(n + 1):
        for a3 in range(n + 1):
            if (a1 + a2)%2 == (a2 + a3)%3 == (a1 + a2 + a3)%5 == 0:
                sums.append(a1 + a2 + a3)

print(max(sums))