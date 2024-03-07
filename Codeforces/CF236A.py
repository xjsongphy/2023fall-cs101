"""于2023-8-31测试通过"""
str_input = input()
set_str = set(str_input)

if len(set_str) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')