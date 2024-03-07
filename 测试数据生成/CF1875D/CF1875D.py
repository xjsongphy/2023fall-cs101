from random import randrange
from itertools import permutations
import json

index = 9
ls = list(range(0, 1000))
ls.reverse()
while True:
    t1 = randrange(0, 1000)
    t2 = randrange(0, 1000)
    if t1 != t2:
        ls[t1], ls[t2] = ls[t2], ls[t1]
    min_num = ls[0]
    count = 1
    for i in ls:
        if i < min_num:
            min_num = i
            count += 1
    if 300 <= count <= 500:
        with open(f'{index}.json', 'w') as file:
            json.dump(ls, file)
        index += 1
        print(index - 1)
        input()
    print(count)