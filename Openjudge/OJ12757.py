"""于2023-9-11测试通过"""
total_sum = 0
temp_sum = 0
dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

words = input().split()
for i in range(len(words)):
    word = words[i]
    if word == 'million':
        total_sum += temp_sum * 1000000
        temp_sum = 0
    elif word == 'hundred':
        if 'thousand' in words[i:] or 'million' in words[i:]:
            temp_sum *= 100
        else:
            total_sum += temp_sum * 100
            temp_sum = 0
    elif word == 'thousand':
        if 'million' not in words[i:]:
            total_sum += temp_sum * 1000
            temp_sum = 0
    elif word in dict.keys():
        temp_sum += dict[word]

total_sum += temp_sum
if words[0] == 'negative':
    total_sum = - total_sum

print(total_sum)