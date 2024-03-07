import json

ls = list(range(1, 1001))
index = 10
data = ''
for i in range(len(ls)):
    data += f' {i}'*(ls[i] + 1)
    print(i)

with open(f'{index}.in', 'w') as file:
    json.dump(data.lstrip(), file)
