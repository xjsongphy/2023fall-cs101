pairs = []
max_num = 100**3
n = int(input())
nums = [(i + 1)**3 for i in range(1, n)]
for i in range(n - 1):
    for j in range(i, n - 1):
        for k in range(j, n - 1):
            sum_num = nums[i] + nums[j] + nums[k]
            if sum_num in nums:
                pairs.append(f'{chr(nums.index(sum_num) + 2)}{chr(i + 2)}{chr(j + 2)}{chr(k + 2)}')
pairs.sort()
for pair in pairs:
    print(f'Cube = {ord(pair[0])}, Triple = ({ord(pair[1])},{ord(pair[2])},{ord(pair[3])})')