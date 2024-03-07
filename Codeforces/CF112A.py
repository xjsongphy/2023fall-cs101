"""于2023-8-31测试通过"""
str1, str2 = input().lower(), input().lower()

if str1 > str2:
    print(1)
elif str1 == str2:
    print(0)
else:
    print('-1')