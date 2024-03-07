"""于2023-11-3使用C++测试通过"""
n, m = map(int, input().split())
charm = list(map(int, input().split()))
dp = [[[0, charm[1]][charm[0] <= i + 1] for i in range(m)] + [0]]
for i in range(1, n):
    dp.append([0]*(m + 1))
    charm = list(map(int, input().split()))
    for j in range(m):
        if charm[0] <= j + 1:
            dp[i][j] = max(dp[i - 1][j], charm[1] + dp[i - 1][j - charm[0]])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-2])

# #include<iostream>
# using namespace std;
#
# int main()
# {
#     int n, m, w, d;
#     cin >> n >> m;
#     cin >> w >> d;
#     int dp[12881] = { 0 };
#     int new_dp[12881] = { 0 };
#
#     for (int i = 1; i < m + 1; i++)
#     {
#         if (w <= i)
#         {
#             dp[i] = d;
#         }
#     }
#     for (int i = 0; i < n - 1; i++)
#     {
#         cin >> w >> d;
#         for (int j = 1; j < m + 1; j++)
#         {
#             new_dp[j] = dp[j];
#             if (w <= j)
#             {
#                 new_dp[j] = max(dp[j], d + dp[j - w]);
#             }
#         }
#         for (int j = 1; j < m + 1; j++)
#         {
#             dp[j] = new_dp[j];
#         }
#     }
#     cout << new_dp[m];
#     return 0;
# }