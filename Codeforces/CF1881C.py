""""""
for _ in range(int(input())):
    n = int(input())
    m = [input() for i in range(n)]
    s = 0
    for i in range(n//2):
        for j in range(n - 1 - 2*i):
            t = n - 1 - i
            ls = [ord(k) for k in [m[i][i + j], m[i + j][t], m[t][t - j], m[t - j][i]]]
            s += 4*max(ls) - sum(ls)
    print(s)