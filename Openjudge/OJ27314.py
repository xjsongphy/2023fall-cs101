"""于2023-12-18测试通过"""
string = input().lower()
before, after = map(str, input().split())
before = before.lower()
after = after.lower()
space = ''
for s in string:
    space += [' ', '1'][s == ' ']

space = space.split()
raw_string = string
string = string.split()
for i in range(len(string)):
    if string[i] == before:
        string[i] = after
    elif string[i] == before + ',':
        string[i] = after + ','
    elif string[i] == before + '.':
        string[i] = after + '.'
    if not i:
        continue
    else:
        string[0] = string[0].title()
    if string[i - 1][-1] == '.':
        string[i] = string[i].title()
ans = ''
if raw_string[0] == ' ':
    for i in range(len(space)):
        ans += ' '*len(space[i]) + string[i]
else:
    for i in range(len(space)):
        ans += string[i] + ' '*len(space[i])
if raw_string[-1] == ' ':
    ans += ' '*len(space[-1])
else:
    ans += string[-1]
print(ans)