"""于2023-11-24测试通过"""
for _ in range(int(input())):
    ans = 0
    s = int(input())
    input()
    b = {}
    a = list(map(int, input().split()))
    input()
    for i in list(map(int, input().split())):
        if b.get(i):
            b[i] += 1
        else:
            b[i] = 1
    for i in a:
        if b.get(s - i):
            ans += b[s - i]
    print(ans)