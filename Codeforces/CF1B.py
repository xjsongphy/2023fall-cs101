"""于2023-11-3测试通过"""
from re import match

word = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
    s = input()
    if match(r'R[0-9]+C[0-9]+', s):
        s = s.removeprefix('R')
        s = list(map(int, s.split('C')))
        index = []
        while s[1] > 0:
            if s[1] % 26:
                index.append(word[s[1] % 26])
                s[1] = s[1] // 26
            else:
                index.append('Z')
                s[1] = s[1] // 26 - 1
        index.reverse()
        index = ''.join(index)
        print(f'{index}{s[0]}')
    else:
        index = 0
        while s[index] in word:
            index += 1
        a = s[:index]
        c = 0
        t = 1
        for i in range(len(a)):
            c += t * word.index(a[len(a) - i - 1])
            t *= 26
        print(f'R{s[index:]}C{c}')

# def match(s):
#     for i in range(1, len(s)):
#         if s[-i] == 'C':
#             if i != len(s) and s[-1 - i] in num and s[1 - i] in num:
#                 return True
#             else:
#                 return False
#     return False
#
#
# word = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# num = '1234567890'
# for _ in range(int(input())):
#     s = input()
#     if match(s):
#         s = s.removeprefix('R')
#         s = list(map(int, s.split('C')))
#         index = []
#         while s[1] > 0:
#             index.append(word[s[1] % 26])
#             s[1] = s[1] // 26
#         index.reverse()
#         index = ''.join(index)
#         print(f'{index}{s[0]}')
#     else:
#         index = 0
#         while s[index] in word:
#             index += 1
#         a = s[:index]
#         c = 0
#         t = 1
#         for i in range(len(a)):
#             c += t*word.index(a[len(a) - i - 1])
#             t *= 26
#         print(f'R{s[index:]}C{c}')