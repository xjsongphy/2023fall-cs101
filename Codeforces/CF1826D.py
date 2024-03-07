"""于2023-12-15参考答案测试通过"""
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    m_1 = ls[0] + 1
    m_2 = ls[n - 1] - n
    dp_1 = [m_1]
    dp_2 = [m_2]

    for i in range(1, n):
        m_1 = max(m_1, ls[i] + i + 1)
        dp_1.append(m_1)
        m_2 = max(m_2, ls[n - 1 - i] - (n - i))
        dp_2.append(m_2)
    ans = max([dp_1[j - 2] + ls[j - 1] + dp_2[n - 1 - j] for j in range(2, n)])
    print(ans)