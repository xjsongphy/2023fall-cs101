""""""
n = int(input())
stations_for_num = {input(): i for i in range(n)}
num_for_station = {value: key for key, value in stations_for_num.items()}

m = int(input())
for i in range(m):
    start, end = map(str, input().split())
    start = stations_for_num[start]
    end = stations_for_num[end]
    if start <= end:
        for j in range(start, end + 1):
            if j != start:
                print(' ', end='')
            print(num_for_station[j], end='')
    else:
        j = start
        while j >= end:
            if j != start:
                print(' ', end='')
            print(num_for_station[j], end='')
            j -= 1
    print()
