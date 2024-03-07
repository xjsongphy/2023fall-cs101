"""于2023-10-7测试通过"""
def f(x):
    return x**3 - 5*(x**2) + 10*x - 80


left, right = 5, 6
while right - left > 0.0000000001:
    length = right - left
    f_left, f_right = f(left), f(right)
    if f_left*f_right > 0:
        if abs(f_left) > abs(f_right):
            left = right
            right += length
        else:
            right = left
            left += length
    elif f_left == 0.0000000000:
        print('%.9f' % left)
    elif f_right == 0.0000000000:
        print('%.9f' % right)
    else:
        middle = (left + right)/2
        f_middle = f(middle)
        if f_middle*f_left > 0:
            left = middle
        else:
            right = middle

middle = (left + right)/2
print('%.9f' % middle)