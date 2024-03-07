"""于2023-12-24测试通过"""
s = input()
n = len(s)
nums = {str(i): 1 for i in range(10)}


def func(s):
    if '[' not in s:
        return s
    i, j = 0, len(s) - 1
    pre = ''
    while True:
        if s[i] == '[':
            break
        pre += s[i]
        i += 1
    count = 1
    j = i + 1
    while True:
        if s[j] == '[':
            count += 1
        elif s[j] == ']':
            count -= 1
            if not count:
                break
        j += 1
    k = i + 1
    num = ''
    while True:
        if s[k] not in nums:
            break
        num += s[k]
        k += 1
    return pre + int(num)*func(s[k:j]) + func(s[j + 1:])


print(func(s))
