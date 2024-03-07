"""于2023-8-31测试通过"""
sentence = input()
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()

sentence = list(sentence)
for i in range(0, len(sentence)):
    if 65 <= ord(upper_sentence[i]) <= 90:
        if sentence[i] == upper_sentence[i]:
            sentence[i] = lower_sentence[i]
        else:
            sentence[i] = upper_sentence[i]

print(''.join(sentence))