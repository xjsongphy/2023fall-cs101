"""于2023-12-23测试通过"""
def judge(s, t):
    ls, lt = len(s), len(t)
    j = 0
    for i in range(ls):
        found = False
        while j < lt:
            if t[j] == s[i]:
                j += 1
                found = True
                break
            j += 1
        if not found:
            return False
    return True


while True:
    try:
        s, t = input().split()
    except EOFError:
        break
    print('Yes' if judge(s, t) else 'No')