"""于2023-12-28测试通过"""
while True:
    n = int(input())
    if not n:
        break
    t = list(map(int, input().split()))
    k = list(map(int, input().split()))
    t.sort()
    k.sort()


    def func(t, k):
        k_j = t_j = n - 1
        ans = k_k = t_k = 0
        for i in range(n):
            if k[k_j] < t[t_j]:
                k_j -= 1
                t_j -= 1
                ans += 3
            elif k[k_j] > t[t_j]:
                ans += 1
                t_k += 1
                k_j -= 1
            else:
                if k[k_k] < t[t_k]:
                    k_k += 1
                    t_k += 1
                    ans += 3
                else:
                    if k[k_j] == t[t_k]:
                        ans += 1
                    ans += 1
                    k_j -= 1
                    t_k += 1
        return ans
    print(func(k, t), 4*n - func(t, k))
