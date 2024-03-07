"""于2023-8-31测试通过"""
str_input = input()
str_wanted = 'hello'

yes_or_no = True

for i in range(0, len(str_wanted)):
    if str_wanted[i] in str_input:
        index = str_input.find(str_wanted[i])

        if index == len(str_input) - 1:
            str_input = ''
        else:
            str_input = str_input[index + 1:]
    else:
        yes_or_no = False
        break

if yes_or_no:
    print('YES')
else:
    print('NO')