"""于2023-10-25测试通过"""
for _ in range(int(input())):
    n = int(input())
    a_s = list(map(int, input().split()))
    data = {}    #[num, sum_low]
    length = total = edge_up = 0
    for i in range(n):
        if data.get(a_s[i]):
            data[a_s[i]][0] += 1
        else:
            data[a_s[i]] = [1, 0]
            length += 1
    if length == 1:
        print(data[a_s[0]][0] // 2)
        continue
    a_s = sorted(list(data.keys()))
    for i in range(1, length):
        data[a_s[length - i - 1]][1] = data[a_s[length - i]][0] + data[a_s[length - i]][1]
    for i in range(length):
        if data[a_s[i]][1] > edge_up:
            total += data[a_s[i]][0]*(data[a_s[i]][1] - edge_up)
            edge_up += data[a_s[i]][0]
    print(total)
