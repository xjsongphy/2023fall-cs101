"""于2023-9-21测试通过"""
n, m = map(int, input().split())
images = [[int(j) for j in input().split()] for i in range(n)]
processed_images = []

for i in range(n):
    if i == 0 or i == n - 1:
        processed_images.append([str(j) for j in images[i]])
    else:
        line = []
        for j in range(m):
            if j == 0 or j == m - 1:
                line.append(str(images[i][j]))
            else:
                num = images[i][j] + images[i - 1][j] + images[i + 1][j] + images[i][j - 1] + images[i][j + 1]
                num /= 5
                if num % 1 > 0.5:
                    num = int(num) + 1
                else:
                    num = int(num)

                line.append(str(num))
        processed_images.append(line)

for i in range(n):
    print(' '.join(processed_images[i]))
