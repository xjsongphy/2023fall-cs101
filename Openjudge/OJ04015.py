"""于2023-8-31测试通过"""
# while True:
#     try:
#         str_input = input()
#
#         if str_input.count('@') != 1:
#             print('NO')
#         elif str_input[0] == '@' or str_input[0] == '.':
#             print('NO')
#         elif str_input[-1] == '@' or str_input[-1] == '.':
#             print('NO')
#         else:
#             at_index = str_input.index('@')
#             if str_input[at_index:].count('.') == 0:
#                 print('NO')
#             elif str_input[at_index + 1] == '.' or str_input[at_index - 1] == '.':
#                 print('NO')
#             else:
#                 print('YES')
#     except EOFError:
#         break

from re import match

try:
    while True:
        print(['NO', 'YES'][match(r'^(([^\.@]+[^@]*[^\.@]+)|([^\.@]))@[^\.@]+\.[^@]*[^\.@]+$', input().strip()) != None])
except EOFError:
    pass