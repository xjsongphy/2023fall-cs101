"""于2023-10-11测试通过"""
for i in range(int(input())):
    print(['NO', 'YES'][360 % (180 - int(input())) == 0])