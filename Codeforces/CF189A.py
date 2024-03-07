""""""
n, a, b, c = map(int, input().split())
a, b, c = map(int, sorted([a, b, c]))
m_a = n//a
count = 0
while m_a >= 0:
    l_a = n - m_a*a
    if not l_a:
        count = max(count, m_a)
        break
    m_b = l_a//b
    while m_b >= 0:
        l_b = l_a - m_b*b
        if not l_b % c:
            count = max(count, m_a + m_b + l_b//c)
            break
        m_b -= 1
    m_a -= 1
print(count)