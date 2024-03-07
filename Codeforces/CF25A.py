"""于2023-8-31测试通过"""
n = int(input())
num_list = input().split()

for i in range(0, n):
    num_list[i] = int(num_list[i])

odd_or_even_list = [x % 2 for x in num_list]
odd = odd_or_even_list.count(0)

if odd == 1:
    for i in range(0, n):
        if odd_or_even_list[i] == 0:
            print(i + 1)
            break
else:
    for i in range(0, n):
        if odd_or_even_list[i] == 1:
            print(i + 1)
            break