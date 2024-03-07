"""于2023-8-31测试通过"""
n = int(input())
total = 0
for i in range(0, n):
    sentence = input()
    total += sentence.count('###') / 2 - sentence.count('### ###')

print(int(total))