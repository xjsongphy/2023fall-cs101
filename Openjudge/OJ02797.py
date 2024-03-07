"""于2023-10-9测试通过"""
words = []
length = []
try:
    while True:
        inputs = input()
        words.append(list(inputs))
        length.append(len(inputs))

except EOFError:
    total = len(words)
    shortest = [[] for i in range(total)]
    shortest_len = [0 for i in range(total)]
    for i in range(total):
        for j in range(total):
            if i == j or shortest_len[i] >= length[j]:
                continue

            if shortest[i] == words[j][:shortest_len[i]]:
                for k in range(shortest_len[i], min(length[i], length[j])):
                    if words[i][k] == words[j][k]:
                        shortest[i].append(words[j][k])
                        shortest_len[i] += 1

                        shortest_len[j] = shortest_len[i]
                        shortest[j] = shortest[i][:]
                    else:
                        break

        print(f"{''.join(words[i])} {''.join(words[i][:shortest_len[i] + 1])}")
