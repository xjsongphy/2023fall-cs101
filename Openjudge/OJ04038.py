from heapq import heapify, heappop, heappush

n, m, k = map(int, input().split())
d = list(map(int, input().split()))
t = [0 for i in range(n + 1)]
on, off = t, t[:]
sum_on_time, start_time = t[:], t[:]
for i in range(m):
    ti, ai, bi = map(int, input().split())
    on[ai] += 1
    off[bi] += 1
    sum_on_time[ai] += ti
    start_time[ai] = max(start_time[ai], ti)

nums = [0]*n
for i in range(1, n):
    nums[i] = nums[i - 1] + on[i] - off[i]

total = arr_time = 0
for i in range(1, n):
    total += d[i - 1]*nums[i]
    start = max(start_time[i], arr_time)
    total += start*on[i] - sum_on_time[i] + (start - arr_time)*(nums[i - 1] - off[i])
    arr_time = start + d[i - 1]
heap = []
heapify(heap)


def cut(i, j):
    if i >= j:
        return
    arr_time = start_time[i]
    while d[i - 1] == 0:
        i += 1
        if i == j:
            return
    k = i + 1
    sub = nums[i]
    max_k = d[i - 1]
    while k <= j:
        t = start_time[k]
        if arr_time <= t or k == j:
            heappush(heap, (-sub, -max_k, i, k))
            if k >= j:
                return
            i = k
            arr_time = start_time[i]
            while d[i - 1] == 0:
                i += 1
                if i == j:
                    return
            k = i + 1
            sub = nums[i]
            max_k = d[i - 1]
        elif t > 0:
            arr_time += d[k - 1]
            sub += on[i]
            max_k = min(max_k, arr_time - t)


cut(1, n)
while k > 0 and len(heap):
    sub, max_k, i, j = heappop(heap)
    max_k = -max_k
    num = min(k, max_k)
    d[i - 1] -= num
    total += sub*num
    k -= num
    cut(i, j)
print(total)