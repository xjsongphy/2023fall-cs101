"""与2023-9-16测试通过"""
n, m = map(int, input().split())
dnas_dict = {}   #num:[dna1, dna2]
words = ['T', 'G', 'C', 'A']
dnas = None

for i in range(m):
    dnas = list(input())
    num = 0
    for j in range(n):
        dnas_part = dnas[j + 1:]
        for word in words[words.index(dnas[j]) + 1:]:
            num += dnas_part.count(word)

    if num in dnas_dict.keys():
        dnas_dict[num].append(''.join(dnas))
    else:
        dnas_dict[num] = [''.join(dnas)]

nums = sorted(dnas_dict.keys())
for num in nums:
    for dna in sorted(dnas_dict[num]):
        print(''.join(dna))
