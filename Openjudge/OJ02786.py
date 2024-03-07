"""于2023-11-21测试通过"""
ls = [1, 2]
while True:
    new = (2*ls[-1] + ls[-2]) % 32767
    if new == 2 and ls[-1] == 1:
        t = len(ls) - 1
        ls.pop()
        break
    ls.append(new)
for _ in range(int(input())):
    print(ls[(int(input()) - 1) % t])
