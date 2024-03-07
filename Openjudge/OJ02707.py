"""于2023-8-31测试通过"""
from math import sqrt

n = int(input())
for i in range(0, n):
    input_list = input().split()
    a = float(input_list[0])
    b = float(input_list[1])
    c = float(input_list[2])

    delta = b ** 2 - 4 * a * c

    if delta == 0.00000:
        x = - b / (2 * a)

        if x == 0.0:
            x = 0.00000

        print('x1=x2=', end='')
        print('%.5f' % x)
    elif delta > 0:
        x1 = (- b + sqrt(delta)) / (2 * a)
        x2 = (- b - sqrt(delta)) / (2 * a)

        if x1 == 0.00000:
            x1 = 0.00000
        if x2 == 0.00000:
            x2 = 0.00000

        print('x1=', end='')
        print('%.5f' % x1, end='')
        print(';x2=', end='')
        print('%.5f' % x2)
    else:
        re_num = - b / (2 * a)
        im_num = sqrt(- delta) / (2 * a)

        if re_num == 0.00000:
            re_num = 0.00000
        if im_num == 0.00000:
            im_num = 0.00000

        print('x1=', end='')
        print('%.5f+' % re_num, end='')
        print('%.5fi' % im_num, end='')
        print(';x2=', end='')
        print('%.5f-' % re_num, end='')
        print('%.5fi' % im_num)