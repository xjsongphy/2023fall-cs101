""""于2023-8-26测试通过"""

year = int(input())

Bool = False

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        Bool = False
    elif year % 3200 == 0:
        Bool = False
    else:
        Bool = True
else:
    Bool = False

if Bool:
    print('Y')
else:
    print('N')