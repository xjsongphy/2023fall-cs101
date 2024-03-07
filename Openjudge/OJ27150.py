from re import match

string = input()
odds = '13579'
odds_fix = '12 36 44 52 76 92'.split()
evens_fix = '16 24 32 56 64 72 96'.split()

if '8' in string :
    print('YES')
    print('8')
    exit()
elif '0' in string:
    print('YES')
    print('0')
    exit()
for fix in evens_fix:
    if match(rf'[0-9]*{fix[0]}[0-9]*{fix[1]}[0-9]*', string):
        print('YES')
        print(fix)
        exit()
for fix in odds_fix:
    if match(rf'[0-9]*[13579]+[0-9]*{fix[0]}[0-9]*{fix[1]}[0-9]*', string):
        print('YES')
        for s in string:
            if s in odds:
                print(s + fix)
                exit()
print('NO')