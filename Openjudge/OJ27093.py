""""""
n, d = map(int, input().split())
h = list(map(int, input().split()))
out = {i: False for i in range(n)}
ans = []
while len(ans) < n:
    i = 0
    new_out = []
    minh = 0
    maxh = float('inf')
    while i < n:
        if out[i]:
            i += 1
            continue
        if len(new_out) == 0:
            new_out.append(h[i])
            minh = maxh = h[i]
            out[i] = True
            i += 1
            continue
        maxh = max(h[i], maxh)
        minh = min(h[i], minh)
        if maxh-h[i] <= d and h[i]-minh <= d:
            new_out.append(h[i])
            out[i] = True
        i += 1
    ans += sorted(new_out)
print(' '.join([str(i) for i in ans]))