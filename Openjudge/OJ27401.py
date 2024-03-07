""""""
n, t = map(int, input().split())
prices = sorted(list(map(int, input().split())))
total = sum(prices)
if total < t:
    print(0)
    exit()

dic = {i: 0 for i in range(t)}
l = dic[0] = 1
keys = [0]
min_t = total
for i in range(n):
    for j in range(l):
        p = keys[j] + prices[i]
        if p > t:
            min_t = min(min_t, p)
            continue
        elif p == t:
            print(t)
            exit()
        if dic[p] == 0:
            dic[p] += 1
            l += 1
            keys.append(p)
print(min_t)
