""""于2023-8-25测试通过"""

N = int(input())
x_list = []
y_list = []

pi = 3.1415926

for i in range(0, N):
    x_and_y = input()
    x_list.append(float(x_and_y.split(' ')[0]))
    y_list.append(float(x_and_y.split(' ')[1]))

for i in range(0, N):
    s = 0.5 * pi * (x_list[i]**2 + y_list[i]**2)
    year = s / 50
    if float(int(year)) != year:
        year = int(year) + 1
    else:
        year = int(year)

    print(f'Property {i + 1}: This property will begin eroding in year {year}.')

print('END OF OUTPUT.')