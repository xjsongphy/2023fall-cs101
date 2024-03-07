"""于2023-10-23测试通过"""
m, n = map(int, input().split())
seats = [[-1 for i in range(n + 2)]]
seats += [[-1] + list(map(int, input().split())) + [-1] for i in range(m)]
seats += [seats[0][:]]
ans = {i: list(map(int, input().split())) for i in range(m*n)}
grades, cheaters = {}, 0
ans[-1] = [-1]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if (ans[seats[i][j]] == ans[seats[i + 1][j]]) + (ans[seats[i][j]] == ans[seats[i][j + 1]]) + (ans[seats[i][j]] == ans[seats[i - 1][j]]) + (ans[seats[i][j]] == ans[seats[i][j - 1]]):
            cheaters += 1
        grade = sum(ans[seats[i][j]])
        if grade in grades:
            grades[grade] += 1
        else:
            grades[grade] = 1
num = 0
for grade in sorted(grades.keys(), reverse=True):
    if num + grades[grade] > 0.4*m*n:
        print(cheaters, num)
        break
    num += grades[grade]