"""于2023-11-27使用C++测试通过"""
ls = [1, 2, 5, 10, 20, 50, 100]
m = int(input())
if m % 50 != 0:
    print('Fail')
    exit()
m = m // 50
count = 0
n, p = [], []
t = list(map(int, input().split()))
for i in range(7):
    c = 1
    while t[i] >= c:
        t[i] -= c
        n.append(c)
        p.append(c*ls[i])
        count += 1
        c *= 2
    if t[i]:
        n.append(t[i])
        p.append(t[i] * ls[i])
        count += 1
dp = [[0] + [float('inf')]*m for _ in range(count)]
dp[0][p[0]] = min(dp[0][p[0]], 1)
for i in range(1, count):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= p[i]:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - p[i]] + n[i])
print(dp[-1][-1] if dp[-1][-1] != float('inf') else 'Fail')


# #include<iostream>
# #include<algorithm>
# using namespace std;
#
# int func(int layor, int left);
#
# int ans = 20001;
# int n[7];
# int ls[7] = { 100, 50, 20, 10, 5, 2, 1 };
#
# int main()
# {
# 	int m;
# 	cin >> m;
# 	for (int i = 0; i < 7; i++)
# 	{
# 		cin >> n[6 - i];
# 	}
# 	if (m % 50 != 0)
# 	{
# 		cout << "Fail";
# 		return 0;
# 	}
# 	m = m / 50;
# 	for (int i = min(n[0], m / ls[0]); i >= 0; i--)
# 	{
# 		int r = func(1, m - i * ls[0]);
# 		if (r >= 0)
# 		{
# 			ans = min(ans, i + r);
# 		}
# 	}
# 	if (ans < 20001)
# 	{
# 		cout << ans;
# 	}
# 	else
# 	{
# 		cout << "Fail";
# 	}
# 	return 0;
# }
#
# int func(int layor, int left)
# {
# 	if (layor == 6 and left <= n[6])
# 	{
# 		return left;
# 	}
# 	else if(layor == 6)
# 	{
# 		return -1;
# 	}
# 	for (int j = min(n[layor], left / ls[layor]); j >= 0; j--)
# 	{
# 		int r = func(layor + 1, left - j * ls[layor]);
# 		if (r >= 0)
# 		{
# 			return r + j;
# 		}
# 	}
# 	return -1;
# }





# ans = 20001
# ls = [100, 50, 20, 10, 5, 2, 1]
# m = int(input())
# n = list(map(int, input().split()))
# n.reverse()
#
# if m % 50 != 0:
#     print("Fail")
#     exit()
# m = m // 50
#
#
# def func(layor, left):
#     if layor == 6 and left <= n[6]:
#         return left
#     elif layor == 6:
#         return -1
#     for j in range(min(n[layor], left // ls[layor]), -1, -1):
#         r = func(layor + 1, left - j * ls[layor])
#         if r >= 0:
#             return r + j
#     return -1
#
#
# for i in range(min(n[0], m // ls[0]), -1, -1):
#     r = func(1, m - i * ls[0])
#     if r >= 0:
#         ans = min(ans, i + r)
# if ans < 20001:
#     print(ans)
# else:
#     print("Fail")


