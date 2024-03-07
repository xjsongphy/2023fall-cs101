"""于2023-9-19测试通过"""
numbers = '1234567890'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = uppers.lower()


def find_elements(formula):
    elements = {}
    for chemical in formula:
        num, chemical = find_pre_nums(chemical)
        while len(chemical) > 0:
            if chemical[0] == '(':
                i = 0
                pairs = 1
                while pairs > 0:
                    i += 1
                    if chemical[i] == '(':
                        pairs += 1
                    elif chemical[i] == ')':
                        pairs -= 1
                inner_elements = find_elements([chemical[1:i]])
                inner_num, chemical = find_pre_nums(chemical[i + 1:])
                for element, counts in inner_elements.items():
                    if element in elements.keys():
                        elements[element] += counts*inner_num*num
                    else:
                        elements[element] = counts*inner_num*num
            elif chemical[0] in uppers:
                if len(chemical) == 1:
                    element = chemical[0]
                    if element in elements.keys():
                        elements[element] += num
                    else:
                        elements[element] = num
                    chemical = ''
                elif chemical[1] in lowers:
                    element = chemical[0:2]
                    inner_num, chemical = find_pre_nums(chemical[2:])
                    if element in elements.keys():
                        elements[element] += num*inner_num
                    else:
                        elements[element] = num*inner_num
                else:
                    element = chemical[0]
                    inner_num, chemical = find_pre_nums(chemical[1:])
                    if element in elements.keys():
                        elements[element] += num*inner_num
                    else:
                        elements[element] = num*inner_num
    return elements


def find_pre_nums(chemical):
    if len(chemical) == 0:
        return 1, ''
    elif chemical[0] not in numbers:
        return 1, chemical
    else:
        i = 0
        while chemical[i] in numbers:
            i += 1
            if i == len(chemical):
                break
        return int(chemical[:i]), chemical[i:]


left = input().split('+')
n = int(input())
rights = [input().split('+') for i in range(n)]
for right in rights:
    link = '=='
    if find_elements(left) != find_elements(right):
        link = '!='
    print('+'.join(left) + link + '+'.join(right))

