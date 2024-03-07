"""于2023-10-9测试通过"""
k = int(input())

for i in range(k):
    w = int(input())
    s = int(input())
    inputs = [int(j) for j in input().split()]
    nv = {inputs[2*j + 1]/inputs[2*j]: [0, 0] for j in range(s)}    #v/n:(n, v)
    for j in range(s):
        nv[inputs[2*j + 1]/inputs[2*j]][0] += inputs[2*j]
        nv[inputs[2*j + 1]/inputs[2*j]][1] += inputs[2*j + 1]

    v_per_n = sorted(nv.keys(), reverse=True)
    total = 0.00
    for j in v_per_n:
        if w >= nv[j][0]:
            w -= nv[j][0]
            total += nv[j][1]
        else:
            total += w*nv[j][1]/nv[j][0]
            break
    print('%.2f' % total)
