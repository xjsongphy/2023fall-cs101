"""于2023-12-20测试通过"""
ls, rs = {}, {}
max_l = min_r = -1
ans = ''
for i in range(int(input())):
    t, l, r = map(str, input().split())
    l, r = int(l), int(r)
    if t == '+':
        if l in ls:
            ls[l] += 1
        else:
            ls[l] = 1
        if r in rs:
            rs[r] += 1
        else:
            rs[r] = 1
        if max_l == -1:
            max_l = l
        else:
            max_l = max(max_l, l)
        if min_r == -1:
            min_r = r
        else:
            min_r = min(min_r, r)
    else:
        ls[l] -= 1
        rs[r] -= 1
        if rs[r] == 0:
            del rs[r]
            if r == min_r:
                if rs:
                    min_r = min(rs.keys())
                else:
                    max_l = min_r = -1
        if ls[l] == 0:
            del ls[l]
            if l == max_l and ls:
                max_l = max(ls.keys())
    ans += ['NO', 'YES'][max_l > min_r] + '\n'
print(ans.rstrip('\n'))