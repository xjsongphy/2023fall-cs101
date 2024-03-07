"""于2023-12-12测试通过"""
while True:
    try:
        string = input()
    except EOFError:
        break
    num_dic = {str(i): 0 for i in range(10)}
    for s in string:
        if s in num_dic:
            num_dic[s] += 1
    for key, value in num_dic.items():
        if value:
            print(f'{key}:{value}')