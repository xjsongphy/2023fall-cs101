# practices = set({})
# while True:
#     inputs = input()
#     if inputs == 'exit':
#         break
#     for i in inputs.split():
#         practices.add(int(i))
#
# print(len(practices))

from time import time
import matplotlib.pyplot as plt

test2, test3, test4 = [], [], []
x_data = []

for i in range(1, 71):
    rounds = int(10**(i / 10))

    start = time()
    ls = []
    for j in range(rounds):
        ls.append(j)
    test2.append(time() - start)

    start = time()
    ls = []
    ls = [i for i in range(rounds)]
    test3.append(time() - start)

    start = time()
    ls = []
    ls = list(range(rounds))
    test4.append(time() - start)

    x_data.append(rounds)
    print('N =', rounds)


# 使用matplotlib绘制折线图，两组数据用不同颜色
plt.plot(x_data, test2, color='blue', label='test2')
plt.plot(x_data, test3, color='red', label='test3')
plt.plot(x_data, test4, color='green', label='test4')

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('time-N')
plt.xlabel('logN')
plt.ylabel('time')

# 显示图形
plt.show()


