from re import match

ls = [i.split('^') for i in input().split('+')]
max_num = 0
for i in ls:
    if match(rf'[0-9]+', i[-1]):
        if i[0][0] != '0' and int(i[-1]) > max_num:
            max_num = int(i[-1])
print(f'n^{max_num}')