""""于2023-8-31测试通过"""
day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
n = int(input())

def guass(num):
    if num >= 0:
        return int(num)
    else:
        return int(num) - 1


def zeller_function(date):
    cy = int(date[0:4])
    m = int(date[4:6])
    d = int(date[6:8])

    if m == 1:
        m = 13
        cy -= 1
    elif m == 2:
        m = 14
        cy -= 1

    c = cy // 100
    y = cy % 100

    # if y == 0 and (m == 13 or m == 14):
    #     y = -1
    #     c = c - 1

    omega = (y + guass(y / 4) + guass(c / 4) - 2 * c + guass(26 * (m + 1) / 10) + d - 1) % 7
    return int(omega)


for i in range(0, n):
    date = input()
    omega = zeller_function(date)
    print(day_list[omega])
