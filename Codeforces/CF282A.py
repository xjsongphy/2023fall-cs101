"""于2023-9-6测试通过"""
n = int(input())
count = 0
for i in range(n):
    input_string = input()

    if '++' in input_string:
        count += 1
    elif '--' in input_string:
        count -= 1
print(count)