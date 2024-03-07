"""于2023-9-16测试通过"""
def similar(word):
    outputs = []
    for dict_word in dicts:
        if len(dict_word) == len(word):
            dif = sum([dict_word[i] != word[i] for i in range(len(word))])
            if dif <= 1:
                outputs.append(dict_word)
        else:
            moves = i = j = 0
            if len(dict_word) - len(word) == 1:
                while i < len(word) and j < len(dict_word):
                    moves += (word[i] != dict_word[j])
                    i += (word[i] == dict_word[j])
                    j += 1
                if moves <= 1:
                    outputs.append(dict_word)
            elif len(word) - len(dict_word) == 1:
                while i < len(dict_word) and j < len(word):
                    moves += (word[j] != dict_word[i])
                    i += (word[j] == dict_word[i])
                    j += 1
                if moves <= 1:
                    outputs.append(dict_word)
    return outputs


dicts = []
while True:
    word = input()
    if word == '#':
        break
    dicts.append(word)

while True:
    word = input()
    if word == '#':
        break
    elif word in dicts:
        print(f'{word} is correct')
    else:
        similars = similar(word)
        similars.insert(0, word + ':')
        print(' '.join(similars))