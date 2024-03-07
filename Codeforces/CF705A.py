"""于2023-9-6测试通过"""
n = int(input())
bool_of_hate = True
output_list = []
for i in range(n):
    if i > 0:
        output_list.append('that')
    if bool_of_hate:
        output_list.append('I hate')
        bool_of_hate = False
    else:
        output_list.append('I love')
        bool_of_hate = True

output_list.append('it')
print(' '.join(output_list))