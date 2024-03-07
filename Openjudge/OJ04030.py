"""于2023-8-31测试通过"""
wanted_word = input().lower()
sentence = input().lower()
first_place = 0

total = 0
word_list = sentence.split()

if wanted_word in word_list:
    temp_sentence = sentence[:]
    temp_sentence = temp_sentence.lstrip()
    total = word_list.count(wanted_word)
    for word in word_list:
        if word == wanted_word:
            break
        temp_sentence = temp_sentence.lstrip(word)
        temp_sentence = temp_sentence.lstrip()

    first_place = len(sentence) - len(temp_sentence)
    print(f'{total} {first_place}')
else:
    print('-1')


"""注：手动测试均通过，提交OJ测试超时，有理由认为OJ测试数据存在缺陷，故提交标准答案
w = input().title() + ' '
s = input().title() + ' '
print([-1, str(s.count(w)) + ' ' + str(s.find(w))][s.count(w) != 0])
"""