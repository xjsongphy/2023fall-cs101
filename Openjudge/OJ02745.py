"""于2023-9-6测试通过"""
num_dict = {0: [1, 1, 1, 0, 1, 1, 1], 1: [0, 0, 1, 0, 0, 1, 0], 2: [1, 0, 1, 1, 1, 0, 1], 3: [1, 0, 1, 1, 0, 1, 1], 4: [0, 1, 1, 1, 0, 1, 0], 5: [1, 1, 0, 1, 0, 1, 1], 6: [1, 1, 0, 1, 1, 1, 1], 7: [1, 0, 1, 0, 0, 1, 0], 8:[1, 1, 1, 1, 1, 1, 1], 9:[1, 1, 1, 1, 0, 1, 1]}

while True:
    inputs = input().split()
    s = int(inputs[0])
    nums = [int(x) for x in inputs[1]]
    if s == 0:
        break

    lines = []
    for i in range(5):
        if i in [0, 2, 4]:
            lines.append([])
            for num in nums:
                lines[-1].append([' ' + ' '*s + ' ', ' ' + '-' * s + ' '][bool(num_dict[num][(i//2)*3])])
        else:
            for j in range(s):
                lines.append([])
                for num in nums:
                    lines[-1].append([' ', '|'][num_dict[num][(i//3)*3 + 1]] + ' '*s + [' ', '|'][num_dict[num][(i//3)*3 + 2]])
    for line in lines:
        print(' '.join(line))
    print()