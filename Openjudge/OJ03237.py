""""于2023-8-26测试通过"""

round_num = int(input())

for i in range(0, round_num):
    foot_num = int(input())
    if foot_num % 2 == 0:
        print(str(int(foot_num / 4) + int((foot_num % 4) / 2)) + ' ' + str(int(foot_num / 2)))
    else:
        print('0 0')