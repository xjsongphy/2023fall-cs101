"""于2023-8-31测试通过"""
str_input = input().lower()

word_list = []
count_list = []
i = 0
while len(str_input) > 0:
    word_list.append(str_input[0])
    former_len = len(str_input)
    str_input = str_input.lstrip(word_list[-1])
    count_list.append(former_len - len(str_input))

for i in range(0, len(word_list)):
    print(f'({word_list[i]},{count_list[i]})', end='')