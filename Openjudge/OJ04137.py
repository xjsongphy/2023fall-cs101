""""""
for _ in range(int(input())):
    data = input().split()
    ls = [int(i) for i in data[0]]
    k = int(data[1])
    l = len(ls)
    out = [False]*l


    def ne(s):
        s += 1
        while s < l:
            if not out[s]:
                break
            s += 1
        return s


    for i in range(k):
        s = 0
        while out[s]:
            s += 1
        while s < l:
            ns = ne(s)
            if ns == l:
                out[s] = True
            elif ls[ns] < ls[s]:
                out[s] = True
                break
            s = ns
    ans = ''
    for i in range(l):
        if not out[i]:
            ans += str(ls[i])
    print(ans)