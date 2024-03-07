"""于2023-12-27使用cpp测试通过"""
base = [1 << i for i in range(11)]
while True:
    n, m = map(int, input().split())
    if not n*m:
        break
    data = list(map(int, input().split()))
    raw_values = data[:n]
    nums = data[n:]
    dp = [0]*(m + 1)
    ls = [0]
    l = 1

    def add(value):
        global l
        for j in range(l):
            t = ls[j] + value
            if t > m:
                continue
            if dp[t]:
                continue
            dp[t] = 1
            l += 1
            ls.append(t)

    for i in range(n):
        idx = 0
        while nums[i] >= base[idx]:
            t = base[idx]
            nums[i] -= t
            add(t * raw_values[i])
            idx += 1
        if nums[i] == 0:
            continue
        add(nums[i] * raw_values[i])
    print(l - 1)
    

