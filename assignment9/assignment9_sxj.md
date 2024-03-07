# Assignment #9: 密集期中考试周

Updated 1918 GMT+8 Nov 6, 2023

2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 必做题目

### OJ19943：图的拉普拉斯矩阵

matrix, http://cs101.openjudge.cn/practice/19943/



思路：边读取数据边进行操作



##### 代码

```python
n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][a] += 1
    matrix[b][b] += 1
    matrix[a][b] -= 1
    matrix[b][a] -= 1
for i in range(n):
    print(' '.join([str(s) for s in matrix[i]]))
```



代码运行截图 

![image-20231109151650260](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311091516398.png)



### OJ19942：⼆维矩阵上的卷积运算v0.2

matrix, http://cs101.openjudge.cn/practice/19942/



思路：依次将卷积核中的元素一次乘到矩阵的元素中，存储到输出矩阵的对应位置



##### 代码

```python
m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
kernel = [list(map(int, input().split())) for _ in range(p)]
ans = [[0]*(n - q + 1) for _ in range(m - p + 1)]

for i in range(p):
    for j in range(q):
        for r in range(m - p + 1):
            for s in range(n - q + 1):
                ans[r][s] += matrix[i + r][j + s]*kernel[i][j]

for i in range(m - p + 1):
    print(' '.join([str(j) for j in ans[i]]))
```



代码运行截图 

![image-20231109151736916](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311091517040.png)



### CF313B: Ilya and Queries

dp/implementation, 1100, https://codeforces.com/contest/313/problem/B



思路：类似前缀和的动态规划



##### 代码

```python
s, m = input(), int(input())
dp = [0, s[0] == s[1]]
for i in range(1, len(s) - 1):
    dp.append(dp[-1] + (s[i] == s[i + 1]))
dp.append(dp[-1])
for _ in range(m):
    l, r = map(int, input().split())
    print(dp[r - 1] - dp[l - 1])
```



代码运行截图 

![image-20231109152927579](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311091529656.png)



### CF706B: Interesting drink

binary search/dp/implementation, 1100, https://codeforces.com/problemset/problem/706/B



思路：二分查找，注意数据在列表外的情况



##### 代码

```python
n = int(input())
prices = sorted(list(map(int, input().split())))
for _ in range(int(input())):
    m = int(input())
    if m < prices[0]:
        print(0)
    elif m >= prices[-1]:
        print(n)
    else:
        l, r = 0, n - 1
        while r - l > 1:
            mid = int((l + r)/2)
            if prices[mid] <= m:
                l = mid
            else:
                r = mid
        print([r, r + 1][m == prices[r]])
```



代码运行截图 

![image-20231109155323446](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311091553597.png)



## 2. 选做题目

如果耗时太⻓，直接看解题思路，或者源码

### CF466C: Number of Ways

binary search/brute force/data structures/dp/two pointers, 1700

https://codeforces.com/problemset/problem/466/C



思路：将前缀和和对应的索引存储为字典方便查找，计算后缀和的同时检验所有数字的和是否等于后缀和的3倍，若等于在已经存储的字典中取出前缀和等于后缀和的索引，二分查找定位到满足要求的索引



##### 代码

```python
n = int(input())
nums = list(map(int, input().split()))
l_sums = {}
r_sum = l_sum = count = 0
total = sum(nums)
for i in range(n):
    l_sum += nums[i]
    if l_sums.get(l_sum):
        l_sums[l_sum].append(i + 2)
    else:
        l_sums[l_sum] = [i + 2]
for i in range(n):
    r_sum += nums[n - 1 - i]
    ls = l_sums.get(total - 2*r_sum)
    if total == 3*r_sum and ls:
        if ls[-1] <= n - i - 1:
            count += len(ls)
        elif ls[0] <= n - i - 1:
            l, r = 0, len(ls) - 1
            while r - l > 1:
                mid = int((l + r) / 2)
                if ls[mid] <= n - i - 1:
                    l = mid
                else:
                    r = mid
            count += [r, r + 1][n - i - 1 == ls[r]]
print(count)
```



代码运行截图 

![image-20231109224403086](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311092244199.png)



经过提示优化了算法（运行时间为三分之一）：

```python
n = int(input())
nums = list(map(int, input().split()))
count = 0
l_sum = total = 0
all_sum = sum(nums)
for i in range(n):
    l_sum += nums[i]
    if 0 < i < n - 1 and l_sum == all_sum * 2 / 3:
        total += count
    if l_sum == all_sum/3:
        count += 1
print(total)
```



代码运行截图

![image-20231109231338642](C:/Users/宋昕杰/AppData/Roaming/Typora/typora-user-images/image-20231109231338642.png)



### CF1443C: The Delivery Dilemma

binary search/greedy/sortings, 1400,

https://codeforces.com/problemset/problem/1443/C
提示： 1）结果要⼀起输出，不要分次print，会超时。2）⽤zip函数。



思路：排序后找到分界点并存储结果，最后统一输出



##### 代码

```python
outputs = []
for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    ls = [(a[i], b[i]) for i in range(n)] + [(0, 0)]
    ls.sort(key=lambda t: t[0], reverse=True)
    dp = [ls[0][0]]
    b_sum = 0
    has_ans = False
    for i in range(n):
        b_sum += ls[i][1]
        dp.append(max(b_sum, ls[i + 1][0]))
        if dp[-1] > dp[-2]:
            outputs.append(dp[-2])
            has_ans = True
            break
    if not has_ans:
        outputs.append(dp[-1])
for ans in outputs:
    print(ans)
```



代码运行截图 

![image-20231110103111073](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202311101031156.png)



## 3. 学习总结和收获

​	深刻体会了python中输出耗时较大。

​	截至2023年11月10日，OJ完成题目102道，CF完成题目44道。





