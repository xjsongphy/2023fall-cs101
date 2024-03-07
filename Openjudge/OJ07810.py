"""于2023-12-27测试通过"""
for _ in range(int(input())):
    s = input()
    print('Yes' if '19' in s or int(s) % 19 == 0 else 'No')