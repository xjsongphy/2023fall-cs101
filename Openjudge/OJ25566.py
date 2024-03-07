"""于2023-12-6测试通过"""
n = int(input())
compute, write = [], []
for _ in range(n):
    a, b = map(int, input().split())
    compute.append(a)
    write.append(b)
for i in range(n - 1):
    for j in range(i + 1, n):
        if compute[i] + max(write[i], compute[j] + write[j]) > compute[j] + max(write[j], compute[i] + write[i]) or (compute[i] + max(write[i], compute[j] + write[j]) == compute[j] + max(write[j], compute[i] + write[i]) and compute[i] > compute[j]):
            compute[i], compute[j] = compute[j], compute[i]
            write[i], write[j] = write[j], write[i]
ends = []
compute_time = 0
for i in range(n):
    compute_time += compute[i]
    ends.append(compute_time + write[i])
print(max(ends))