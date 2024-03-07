"""于2023-8-31测试通过"""
n = int(input())
word_list = input().split()

i = 0
output = ''
while i < n:
    if len(output) + len(word_list[i]) + 1 <= 81:
        output += ' ' + word_list[i]
        i += 1
    else:
        print(output.lstrip())
        output = ''

if output != '':
    print(output.lstrip())