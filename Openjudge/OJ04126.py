""""""
for _ in range(int(input())):
    parts = list(set([input() for i in range(int(input()))]))
    n = len(parts)
    dna = parts[0]
    parts[0] = ''
    for i in range(n - 1):
        try:
            for j in [3, 2, 1, 0]:
                for k in range(n):
                    if parts[k]:
                        if dna[:j] == parts[k][-j:]:
                            dna = parts[k][:4-j] + dna
                            parts[k] = ''
                            1/0
                        elif dna[-j:] == parts[k][:j]:
                            dna = dna + parts[k][j:]
                            parts[k] = ''
                            1/0
        except:
            continue
    print(len(dna))