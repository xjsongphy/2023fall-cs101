a = int(input())

if a % 2 != 0:
    print('0 0')
else:
    min_num = a // 4 + (a % 4) // 2
    max_num = a // 2
    print(f'{min_num} {max_num}')