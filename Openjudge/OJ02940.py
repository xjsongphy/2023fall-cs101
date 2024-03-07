"""于2023-12-12测试通过"""
a, n = map(int, input().split())
ans = 0
p = 1
for i in range(n):
    ans += (n - i)*a*p
    p *= 10
print(ans)