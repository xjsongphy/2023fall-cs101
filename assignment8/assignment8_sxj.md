# Assignment #8: Nov 月考

Updated 1355 GMT+8 Nov 2, 2023

2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）1）Nov⽉考： AC6 。题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 必做题目

### 23563: 多项式时间复杂度

string/implementation/math, http://cs101.openjudge.cn/practice/23563





思路：合理利用split()找出系数第一位不为0的最高次数



##### 代码

```python
from re import match

ls = [i.split('^') for i in input().split('+')]
max_num = 0
for i in ls:
    if match(rf'[0-9]+', i[-1]):
        if i[0][0] != '0' and int(i[-1]) > max_num:
            max_num = int(i[-1])
print(f'n^{max_num}')
```



代码运行截图 

![image-20231102163944984](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021639614.png)



### 03143: 验证“歌德巴赫猜想”

math, http://cs101.openjudge.cn/practice/03143



思路：欧拉筛生成素数表，然后在生成一个字典便于查找，最后从第一个素数开始寻找符合要求的结果，直至半数停止。



##### 代码

```python
n = int(input())
if n < 6 or n % 2 != 0:
    print('Error!')
    exit()
nums = {i: 1 for i in range(2, n + 1)}
primes = []
for i in nums:
    if nums[i]:
        primes.append(i)
    for j in primes:
        if i*j > n:
            break
        nums[i*j] = 0
        if not j % i:
            break
primes_dict = {i: 1 for i in primes}
for i in primes:
    if 2 * i > n:
        break
    if primes_dict.get(n - i):
        print(f'{n}={i}+{n - i}')
```



代码运行截图 

![image-20231102164115499](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021641899.png)



### 23566: 决战双十一

implementation, http://cs101.openjudge.cn/practice/23566



思路：合理选取数据结构即可。



##### 代码

```python
n, m = map(int, input().split())
goods = {i:0 for i in range(1, m + 1)}
coupons = {}
total = 0
for _ in range(n):
    s, p = map(int, input().split())
    goods[s] += p
    total += p
total -= (total // 200)*30
for i in range(m):
    q, x = map(int, input().split('-'))
    if goods[i + 1] >= q:
        total -= x
print(total)
```



代码运行截图 

![](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021642925.png)



### 03670: 计算鞍点

matrice, http://cs101.openjudge.cn/practice/03670



思路：找到每行的最大值，验证其是否为该列的最小值。



##### 代码

```python
matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    max_num = max(matrix[i])
    j = matrix[i].index(max_num)
    found = True
    for k in range(5):
        if matrix[k][j] < max_num:
            found = False
            break
    if found:
        print(i + 1, j + 1, max_num)
        exit()
print('not found')
```



代码运行截图 

![image-20231102164345538](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021643925.png)



### 19948: 因材施教

greedy, http://cs101.openjudge.cn/practice/19948



思路：转化为数学问题，所求总体差异等于这组数据的极差减去排序后m-1个某两个数据的差，也就是要求出相邻两个数据差由小到大排序后的前m-1个差的和（代码实现的时候调整了一下正负号使代码精简）



##### 代码

```python
n, m = map(int, input().split())
ranks = sorted(list(map(int, input().split())))
print(ranks[-1] - ranks[0] + sum(sorted([ranks[i] - ranks[i + 1] for i in range(n - 1)])[:m - 1]))
```



代码运行截图 

![](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021651934.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：合理选取数据结构即可。



##### 代码

```python
for _ in range(int(input())):
    n, m, b = map(int, input().split())
    skills = {}
    for i in range(n):
        t, x = map(int, input().split())
        if skills.get(t):
            skills[t].append(x)
        else:
            skills[t] = [x]
    for i in sorted(skills.keys()):
        b -= sum(sorted(skills[i], reverse=True)[:m])
        if b <= 0:
            print(i)
            break
    if b > 0:
        print('alive')
```



代码运行截图 

![image-20231102164519326](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311021645503.png)



## 2. 学习总结和收获

​	这次期中考试中的4道题都做过，所以全部完成用时较快；这周在准备线性代数的期中考试，所以刷题量少了点，期中季过去后继续追进度。

​	截至2023年11月2日，OJ完成题目95道，CF完成题目39道。





