"""于2023-9-6测试通过"""
input_list = input().split()
n = int(input_list[0])
k = int(input_list[1])

score_list = [int(x) for x in input().split()]

total = 0
for score in score_list:
    if score >= score_list[k - 1] and score > 0:
        total += 1
    else:
        break

print(total)