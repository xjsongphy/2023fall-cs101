"""于2023-12-27测试通过"""
from queue import Queue
n, k = map(int, input().split())
if n >= k:
    print(n - k)
    exit()

dp = [False]*(1000001)
q = Queue()
q.put((0, n))
time = 0
while True:
    t, i = q.get()
    if i == k:
        print(t)
        exit()
    if dp[i]:
        continue
    t += 1
    dp[i] = True
    if not dp[i + 1]:
        q.put((t, i + 1))
    if i <= k :
        if not dp[2 * i]:
            q.put((t, 2 * i))
    if i > 0:
        if not dp[i - 1]:
            q.put((t, i - 1))