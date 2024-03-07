year = int(input())

yes_or_no = False
if year % 4 == 0:
    yes_or_no = True
    if year % 100 == 0 and year % 400 != 0:
        yes_or_no = False
    elif year % 3200 == 0:
        yes_or_no = False

if yes_or_no:
    print('Y')
else:
    print('N')