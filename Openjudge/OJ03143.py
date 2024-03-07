""""于2023-8-26测试通过"""

num = int(input())
single_list = []

if num < 6:
    print('Error!')
elif num % 2 != 0:
    print('Error!')
else:
    single_list = [x for x in range(2, num + 1)]

    i = 0
    while i < len(single_list):
        j = 2
        while j * single_list[i] <= single_list[-1]:
            if j * single_list[i] in single_list:
                single_list.remove(j * single_list[i])

            j += 1
        i += 1

    i = 0
    while single_list[i] <= num / 2:
        if num - single_list[i] in single_list:
            print(f'{num}={single_list[i]}+{num - single_list[i]}')

        i += 1