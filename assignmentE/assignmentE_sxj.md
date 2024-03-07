# Assignment #E: 算法基础

Updated 1419 GMT+8 Dec 12, 2023

2023 fall, Complied by Xinjie Song, Phy



**说明：**

本周作业涉及到枚举、贪心、bfs、矩阵，建议提前开始作业，如果耗时太⻓，直接找答案看。两个题解，经常更新。所以最好从这个链接下载最新的，https://github.com/GMyhf/2020fall-cs101 。

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 题目

如果耗时太⻓，直接看解题思路，或者源码



### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692



思路：枚举



##### 代码

```python
def weigh(input_list, weight_list):
    left_weight = 0
    right_weight = 0

    for i in range(0, 4):
        left_weight += weight_list[ord(input_list[0][i]) - 65]
        right_weight += weight_list[ord(input_list[1][i]) - 65]

    if left_weight > right_weight:
        return 'up'
    elif left_weight == right_weight:
        return 'even'
    else:
        return 'down'

n = int(input())
for i in range(0, n):
    input_list_list = []
    for j in range(0, 3):
        input_list_list.append(input().strip().split())

    already_right = False
    for k in range(0, 12):
        weight_list = [0 for x in range(0, 12)]
        weight_list[k] = 1
        right = True
        for x in range(0, 3):
            if weigh(input_list_list[x], weight_list) != input_list_list[x][-1]:
                right = False
                break
        if right:
            print(f'{chr(65 + k)} is the counterfeit coin and it is heavy.')
            already_right = True

    if not already_right:
        for k in range(0, 12):
            weight_list = [0 for x in range(0, 12)]
            weight_list[k] = -1
            right = True
            for x in range(0, 3):
                if weigh(input_list_list[x], weight_list) != input_list_list[x][-1]:
                    right = False
                    already_right = True
                    break
            if right:
                print(f'{chr(65 + k)} is the counterfeit coin and it is light.')
```



代码运行截图 

![image-20231212172217850](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312121722995.png)



### 18164: 剪绳子

greedy/huffman, http://cs101.openjudge.cn/practice/18164/



思路：利用Python的heapq库，考虑将绳子拼回去即可



##### 代码

```python
import heapq

n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
cost = 0
for i in range(n - 1):
    length = heapq.heappop(heap) + heapq.heappop(heap)
    cost += length
    heapq.heappush(heap, length)
print(cost)
```



代码运行截图 

![image-20231212172235974](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312121722076.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：若某个点不能被覆盖，在这个点及以后的点需要位置最小的雷达站的位置安装雷达站，注意浮点数精度问题



##### 代码

```python
from math import sqrt

num = 1
while True:
    n, d = map(int, input().split())
    if n + d == 0:
        break
    x_y = {}
    for _ in range(n):
        x, y = map(int, input().split())
        if x in x_y:
            x_y[x] = max(x_y[x], y)
        else:
            x_y[x] = y
    n = len(x_y)
    count = 1
    x = list(sorted(x_y.keys()))
    try:
        ls = [x[i] + sqrt(d**2 - x_y[x[i]]**2) for i in range(n)]
        for i in range(2, n + 1):
            ls[-i] = min(ls[-i], ls[-i + 1])
        l = ls[0]
        for i in range(1, n):
            if (x[i] - l)**2 + x_y[x[i]]**2 - d**2 > 0.001:
                l = ls[i]
                count += 1
    except ValueError:
        count = -1
    if d < 0:
        count = -1
    print(f'Case {num}: {count}')
    num += 1
    input()
```



代码运行截图 

![image-20231213105517137](C:/Users/宋昕杰/AppData/Roaming/Typora/typora-user-images/image-20231213105517137.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930



思路：模板题



##### 代码

```python
from queue import Queue
m, n = map(int, input().split())
matrix = [[-1]*(n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(m)] + [[-1]*(n + 2)]
ls = Queue()
ls.put((1, 1, 0))
searched = {}
while not ls.empty():
    x, y, step = ls.get()
    if matrix[x][y] == 1:
        print(step)
        exit()
    elif matrix[x][y] in [2, -1] or (x, y) in searched:
        continue
    searched[(x, y)] = 1
    step += 1
    ls.put((x + 1, y, step))
    ls.put((x - 1, y, step))
    ls.put((x, y + 1, step))
    ls.put((x, y - 1, step))
print('NO')
```



代码运行截图 

![image-20231212172329878](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312121723957.png)



### 1163B2. Cat Party (Hard Edition)

https://codeforces.com/contest/1163/problem/B2
好题。通过维护双层（三层？）数据结构可以O(n)。

确实好题，而且感觉难度适合作业没有复杂的东西。多维护了几个数就做到O(n)了。



思路：算法实现较为简单，判断是否满足条件较为复杂，有4种情况



##### 代码

```python
n = int(input())
color = {}
nums = {}
ans = 0
ls = list(map(int, input().split()))
first, second = 0, 0
 
for i in range(n):
    key = ls[i]
    if key in color:
        value = color[key]
        nums[value] -= 1
        if not nums[value]:
            del nums[value]
            if value == second and second + 1 == first:
                second = 0
                for j in nums:
                    if second < j < first:
                        second = j
        value += 1
        color[key] += 1
    else:
        value = color[key] = 1
    if value in nums:
        nums[value] += 1
    else:
        nums[value] = 1
        if value > first:
            if first in nums:
                second = first
            first = value
        elif value > second:
            second = value
    if second == 0 and nums[first] == 1:
        ans = i
    elif first == 1:
        ans = i
    elif first - second == nums[first] == 1 and len(nums) == 2:
        ans = i
    elif second == 1:
        if nums[second] == 1:
            ans = i
print(ans + 1)
```



代码运行截图 

![image-20231213091832105](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312130918243.png)





### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811



思路：很久前看提示做的



##### 代码

```python
map_matrix = []
switch_matrix = []


def switch_on(x, y, matrix):
    if matrix[x][y] == 0:
        matrix[x][y] = 1
    else:
        matrix[x][y] = 0
    if x > 0:
        if matrix[x - 1][y] == 0:
            matrix[x - 1][y] = 1
        else:
            matrix[x - 1][y] = 0
    if y > 0:
        if matrix[x][y - 1] == 0:
            matrix[x][y - 1] = 1
        else:
            matrix[x][y - 1] = 0
    if x < 4:
        if matrix[x + 1][y] == 0:
            matrix[x + 1][y] = 1
        else:
            matrix[x + 1][y] = 0
    if y < 5:
        if matrix[x][y + 1] == 0:
            matrix[x][y + 1] = 1
        else:
            matrix[x][y + 1] = 0

    return matrix


def copy(matrix):
    copy_matrix = []
    for i in range(5):
        copy_matrix.append(matrix[i][:])

    return copy_matrix


for i in range(5):
    map_matrix.append([int(x) for x in input().split()])
    switch_matrix.append([0 for x in range(6)])

while True:
    copy_matrix = copy(map_matrix)
    for i in range(5):
        if i > 0:
            for j in range(6):
                if copy_matrix[i - 1][j] == 1:
                    switch_matrix[i][j] = 1
                else:
                    switch_matrix[i][j] = 0
        for j in range(6):
            if switch_matrix[i][j] == 1:
                copy_matrix = switch_on(i, j, copy_matrix)

    if sum(copy_matrix[4]) == 0:
        break

    switch_matrix[0][0] += 1
    for i in range(6):
        if switch_matrix[0][i] == 2:
            switch_matrix[0][i] = 0
            switch_matrix[0][i + 1] += 1

for i in range(5):
    for j in range(6):
        if j == 5:
            print(switch_matrix[i][j])
        else:
            print(switch_matrix[i][j], end='')
            print(' ', end='')
```



代码运行截图 

![image-20231212172402812](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312121724890.png)



### 02802: 小游戏

dfs, bfs, http://cs101.openjudge.cn/practice/02802/ 



思路：BFS，记录方向



##### 代码

```python
from copy import deepcopy

board = 1
while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    maps = [[] for i in range(h + 2)]
    for i in range(h + 2):
        maps[i].append(0)
        if i == 0 or i == h + 1:
            for j in range(w):
                maps[i].append(0)
        else:
            for j in input():
                maps[i].append([0, 1][j == 'X'])
        maps[i].append(0)

    print(f'Board #{board}:')
    pair = 1
    while True:
        y1, x1, y2, x2 = map(int, input().split())
        if x1 + y1 + x2 + y2 == 0:
            break
        begin = {((x1, y1), 1): '', ((x1, y1), 2): ''}
        end = (x2, y2)

        queue = begin
        next_queue = {}
        searched = {}
        step = 0
        found = False
        while True:
            for i in queue.keys():
                if i[0] == end:
                    print(f'Pair {pair}: {step} segments.')
                    found = True
                    break
                else:
                    searched[i] = 1
                    x = i[0][0]
                    y = i[0][1]
                    if maps[x][y] == 1 and step != 0:
                        continue
                    if i[1] == 1:
                        for j in range(x + 1, h + 2):
                            next = ((j, y), 2)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[j][y] == 1:
                                break
                        for j in range(0, x):
                            next = ((x - 1 - j, y), 2)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x- 1 - j][y] == 1:
                                break
                    else:
                        for j in range(y + 1, w + 2):
                            next = ((x, j), 1)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x][j] == 1:
                                break
                        for j in range(0, y):
                            next = ((x, y - 1 - j), 1)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x][y - 1 - j] == 1:
                                break
            if found:
                break
            if len(next_queue) == 0:
                print(f'Pair {pair}: impossible.')
                break
            queue = deepcopy(next_queue)
            next_queue = {}
            step += 1
        pair += 1
    board += 1
    print()
```



代码运行截图 

![image-20231213110243458](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312131102593.png)



## 2. 学习总结和收获

​	Radar Installation花了点时间，学习到了一些新知识和易错点。

​	截至2023年12月13日，OJ完成题目151道，CF完成题目51道。



