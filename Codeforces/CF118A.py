"""于2023-9-6测试通过"""
output_list = []
input_list = list(input().lower())
string_for_search = 'aoyeui'

for char in input_list:
    if char in string_for_search:
        continue
    else:
        output_list.append('.')
        output_list.append(char)

print(''.join(output_list))