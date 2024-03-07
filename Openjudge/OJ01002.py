"""于2023-9-15测试通过"""
word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
num_list = [str(x) for x in range(10)]
n = int(input())
nums_dict = {}
nums = []

for i in range(n):
    nums = list(''.join(input().lower().split('-')))
    processed_nums = []
    for num in nums:
        if num in num_list:
            processed_nums.append(num)
        else:
            processed_nums.append(str(word_list.index(num) // 3 + 2))
    processed_nums = ''.join(processed_nums)
    if processed_nums in nums_dict.keys():
        nums_dict[processed_nums] += 1
    else:
        nums_dict[processed_nums] = 1

nums_list = sorted(nums_dict.keys())
exist = False
for nums in nums_list:
    if nums_dict[nums] > 1:
        print(str(nums[:3]) + '-' + str(nums[3:]) + ' ' + str(nums_dict[nums]))
        exist = True

if not exist:
    print('No duplicates.')