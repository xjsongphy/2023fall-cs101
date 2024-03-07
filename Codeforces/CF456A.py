""""于2023-8-31测试通过"""
n = int(input())

price_list = []
quality_list = []
dict_of_price_quality = {}

for i in range(0, n):
    str_input = input()
    data_list = str_input.split()
    price_list.append(int(data_list[0]))
    quality_list.append(int(data_list[1]))
    dict_of_price_quality[price_list[-1]] = quality_list[-1]

price_list.sort()
quality_list.sort()

bool_vary = True
for i in range(0, n):
    if dict_of_price_quality[price_list[i]] != quality_list[i]:
        print('Happy Alex')
        bool_vary = False
        break

if bool_vary:
    print('Poor Alex')
