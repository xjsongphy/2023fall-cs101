"""于2023-11-1测试通过"""
for _ in range(int(input())):
    n, m, b = map(int, input().split())
    skills = {}
    for i in range(n):
        t, x = map(int, input().split())
        if skills.get(t):
            skills[t].append(x)
        else:
            skills[t] = [x]
    for t in sorted(skills.keys()):
        b -= sum(sorted(skills[t], reverse=True)[:m])
        if b <= 0:
            break
    print([t, 'alive'][b > 0])