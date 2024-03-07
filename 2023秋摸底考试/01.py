round_num = int(input())
unlocked_num = 0

for i in range(round_num):
    n = int(input())
    cells = [0 for x in range(n)]
    for j in range(n):
        for k in range(n):
            if (k + 1) %  (j + 1) == 0:
                if cells[k] == 1:
                    cells[k] = 0
                else:
                    cells[k] = 1

    print(sum(cells))
