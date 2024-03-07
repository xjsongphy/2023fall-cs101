"""于2023-12-27测试通过"""
ans = 0
dp_vo = 0
dp_v = 0
s = input()
l = len(s)
for i in range(l - 1):
    if s[i] == 'o':
        dp_vo += dp_v
    elif s[i] == s[i + 1] == 'v':
        dp_v += 1
        ans += dp_vo
print(ans)