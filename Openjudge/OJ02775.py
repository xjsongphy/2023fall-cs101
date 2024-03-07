"""于2023-10-16测试通过"""
def main(layer, i):
    files = []
    while i < l:
        if datas[i][0] == 'f':
            files.append(datas[i])
            i += 1
        elif datas[i][0] == 'd':
            print('|     '*(layer + 1) + datas[i])
            i += 1
            i = main(layer + 1, i)
        elif datas[i] == ']':
            break
    for file in sorted(files):
        print('|     '*layer + file)
    return i + 1


count = 1
while True:
    datas, i = [], 0
    while True:
        data = input()
        if data == '*':
            break
        elif data == '#':
            exit()
        datas.append(data)
    l = len(datas)
    print(f'DATA SET {count}:\nROOT')
    main(0, 0)
    print()
    count += 1
