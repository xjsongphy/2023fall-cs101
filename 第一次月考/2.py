months = {}
for i in range(12):
    if i + 1 in [1, 3, 5, 7, 8, 10, 12]:
        months[i + 1] = 31
    elif i + 1 == 2:
        months[2] = 28
    else:
        months[i + 1] = 30

n = int(input())
for i in range(n):
    i_month, i_date, num, f_month, f_date = map(int, input().split())
    days = f_date - i_date
    for j in range(i_month, f_month):
        days += months[j]
    print(num*(2**days))