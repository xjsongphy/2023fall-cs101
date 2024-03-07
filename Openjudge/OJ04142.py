"""于2023-10-14测试通过"""
def f(x):
    return x**5 - 15*(x**4) +85*(x**3) - 225*(x**2) + 274*x - 121


left, right = 1.5, 2.4
while right - left > 0.0000001:
    f_left, f_right = f(left), f(right)
    if f_left == 0.0000000000:
        print('%.6f' % left)
        exit()
    elif f_right == 0.0000000000:
        print('%.6f' % right)
        exit()
    else:
        middle = (left + right)/2
        f_middle = f(middle)
        if f_middle*f_left > 0:
            left = middle
        else:
            right = middle

middle = (left + right)/2
print('%.6f' % middle)