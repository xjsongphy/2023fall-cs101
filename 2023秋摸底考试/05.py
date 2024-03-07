l, m = map(int, input().split())
road_list = [1 for x in range(l + 1)]

for i in range(m):
    begin, end = map(int, input().split())
    for j in range(begin, end + 1):
        road_list[j] = 0

print(sum(road_list))