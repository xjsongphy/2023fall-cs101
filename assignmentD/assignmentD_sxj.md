# Assignment #D: Dec 月考

Updated 1506 GMT+8 Dec 7, 2023

2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）Dec ⽉考： AC5。题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 题目

如果耗时太⻓，直接看解题思路，或者源码



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：欧拉筛



##### 代码

```python
m, n = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
primes = []
lim = 10**4
nums = {i + 1: 1 for i in range(1, 10**4)}
for i in range(2, 10**4 + 1):
    if nums[i]:
        primes.append(i)
    for j in primes:
        if i*j > lim:
            break
        nums[i*j] = 0
        if i % j == 0:
            break
t_primes = {i**2: 1 for i in primes}
for i in range(m):
    count = sum_score = 0
    for j in ls[i]:
        if j in t_primes:
            count += 1
            sum_score += j
    if count:
        print('%.2f' % (sum_score/len(ls[i])))
    else:
        print(0)
```



代码运行截图 

![image-20231208100709766](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081007879.png)



### 18224: 找魔数

http://cs101.openjudge.cn/practice/18224



思路：字典查找



##### 代码

```python
m = int(input())
ls = list(map(int, input().split()))
lim = 32
square = {i**2: 1 for i in range(1, lim)}
key = square.keys()
for i in ls:
    for j in key:
        if j >= i:
            break
        if i - j in square:
            print(bin(i), oct(i), hex(i))
            break
```



代码运行截图 

![image-20231208100840534](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081008607.png)



### 19963: 买学区房

http://cs101.openjudge.cn/practice/19963



思路：常规思路



##### 代码

```python
n = int(input())
distances = [int(i.split(',')[0][1:]) + int(i.split(',')[1][:-1]) for i in input().split()]
prices = [int(i) for i in input().split()]
ddp = [distances[i]/prices[i] for i in range(n)]
sorted_pri = sorted(prices)
sorted_ddp = sorted(ddp)

if n % 2 == 0:
    middle_ddp = (sorted_ddp[n // 2 - 1] + sorted_ddp[n // 2])/2
    middle_pri = (sorted_pri[n // 2 - 1] + sorted_pri[n // 2])/2
else:
    middle_ddp = sorted_ddp[n // 2]
    middle_pri = sorted_pri[n // 2]

total = [ddp[i] > middle_ddp and prices[i] < middle_pri for i in range(n)]
print(sum(total))
```



代码运行截图 

![image-20231208100916061](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081009139.png)



### 23806: 三数之和

http://cs101.openjudge.cn/practice/23806/



思路：输入转成字典，排序后查找省去去重的环节



##### 代码

```python
dic = {}
for i in map(int, input().split()):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
ls = sorted(dic.keys())
n = len(ls)
total = 0
for i in range(n):
    key_i = ls[i]
    if key_i > 0:
        break
    elif key_i == 0:
        total += (dic[key_i] >= 3)
        break
    if dic[key_i] >= 2:
        total += (-2*key_i in dic)
    for j in range(i + 1, n):
        key_j = ls[j]
        t = -key_i - key_j
        if t < key_j:
            break
        if t == key_j:
            total += (dic[t] > 1)
        else:
            total += (t in dic)
print(total)
```

代码运行截图 

![image-20231208122134433](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081221542.png)



### 25561: 2022决战双十一

http://cs101.openjudge.cn/practice/25561/





思路：暴力



##### 代码

```python
n, m = map(int, input().split())
prices = {}
coupons = {}
for i in range(n):
    datas = input().split()
    prices[i] = {}
    for data in datas:
        data = data.split(':')
        prices[i][int(data[0]) - 1] = int(data[1])
for i in range(m):
    datas = input().split()
    coupons[i] = {}
    for data in datas:
        data = data.split('-')
        coupons[i][int(data[0])] = int(data[1])
final = set()


def func(i, shops):
    if i == n:
        total = sum(shops)
        total -= (total//300)*50
        for j in range(m):
            sub = {0}
            for key, value in coupons[j].items():
                if shops[j] >= key:
                    sub.add(value)
            total -= max(sub)
        final.add(total)
        return
    for key, value in prices[i].items():
        t = shops[:]
        t[key] += value
        func(i + 1, t)


func(0, [0]*m)
print(min(final))
```



代码运行截图 

![image-20231208102139799](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081021875.png)



### 08210: 河中跳房子

http://cs101.openjudge.cn/practice/08210/



思路：参考题解



##### 代码

```python
l, n, m = map(int, input().split())
ls = [0] + [int(input()) for _ in range(n)] + [l]
std = l//2
left, right = 0, l
while right - left > 1:
    count = now = 0
    for i in range(1, n + 1):
        if ls[i] - now < std:
            count += 1
        else:
            now = ls[i]
    count += (l - now < std)
    if count <= m:
        left = std
        std = (right + std)//2
    elif count > m:
        right = std
        std = (left + std)//2
print(left)
```



代码运行截图 

![image-20231210092010774](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312100920990.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：常规思路



##### 代码

```python
from math import ceil
while True:
    n = int(input())
    if not n:
        break
    times = []
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        times.append(t + 16200/v)
    print(ceil(min(times)))
```



代码运行截图 

![image-20231208122615927](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202312081226059.png)



## 2. 学习总结和收获

​	河中跳房子虽然可能多次提到，但我还是没做过，考场上也没看出来，遗憾AC5。接下来可以考虑模拟期末考，找几个不同类型的题一起做，或者重点练贪心和动态规划题目。

​	截至2023年12月10日，OJ完成题目145道，CF完成题目50道。





