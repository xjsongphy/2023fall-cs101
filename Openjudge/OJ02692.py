"""于2023-8-31测试通过"""
def weigh(input_list, weight_list):
    left_weight = 0
    right_weight = 0

    for i in range(0, 4):
        left_weight += weight_list[ord(input_list[0][i]) - 65]
        right_weight += weight_list[ord(input_list[1][i]) - 65]

    if left_weight > right_weight:
        return 'up'
    elif left_weight == right_weight:
        return 'even'
    else:
        return 'down'


n = int(input())
for i in range(0, n):
    input_list_list = []
    for j in range(0, 3):
        input_list_list.append(input().strip().split())

    already_right = False
    for k in range(0, 12):
        weight_list = [0 for x in range(0, 12)]
        weight_list[k] = 1
        right = True
        for x in range(0, 3):
            if weigh(input_list_list[x], weight_list) != input_list_list[x][-1]:
                right = False
                break
        if right:
            print(f'{chr(65 + k)} is the counterfeit coin and it is heavy.')
            already_right = True

    if not already_right:
        for k in range(0, 12):
            weight_list = [0 for x in range(0, 12)]
            weight_list[k] = -1
            right = True
            for x in range(0, 3):
                if weigh(input_list_list[x], weight_list) != input_list_list[x][-1]:
                    right = False
                    already_right = True
                    break
            if right:
                print(f'{chr(65 + k)} is the counterfeit coin and it is light.')
