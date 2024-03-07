n, d = map(int, input().split())
height_list = [int(input()) for x in range(n)]
sorted_height_list = sorted(height_list, reverse=True)
height_list.reverse()

for max_height in sorted_height_list:
    const_index = index = height_list.index(max_height)

    while index < n - 1:
        if abs(height_list[const_index] - height_list[index + 1]) > d:
            break
        index += 1
    height_list.insert(index + 1, height_list[const_index])
    del height_list[const_index]

height_list.reverse()
for height in height_list:
    print(height)