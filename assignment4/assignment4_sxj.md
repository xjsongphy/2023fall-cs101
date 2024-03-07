# Assignment #4: 国庆节月考

Updated 1514 GMT+8 Oct 5, 2023



2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**


操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.2 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



## 1. 必做题目

#### 02701: 与7无关的数

math, http://cs101.openjudge.cn/practice/02701

一个正整数,如果它能被7整除,或者它的十进制表示法中某一位上的数字为7,则称其为与7相关的数.现求所有小于等于n(n < 100)的与7无关的正整数的平方和.

**输入**

输入为一行,正整数n(n < 100)

**输出**

输出一行，包含一个整数，即小于等于n的所有与7无关的正整数的平方和。

样例输入

```
21
```

样例输出

```
2336
```

来源

计算概论05



【宋昕杰，物理学院，2023年秋】

思路：首先另写程序计算所有与7无关的正整数，然后存储为列表，根据输入读取列表并计算平方值



##### 代码

```python
n = int(input())
ls = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 36, 38, 39, 40, 41, 43, 44, 45, 46, 48, 50, 51, 52, 53, 54, 55, 58, 59, 60, 61, 62, 64, 65, 66, 68, 69, 80, 81, 82, 83, 85, 86, 88, 89, 90, 92, 93, 94, 95, 96, 99]
result = 0
for i in ls:
    if i <= n:
        result += i**2
    else:
        break
print(result)
```



代码运行截图 

![image-20231005163856795](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051638173.png)



#### 02712: 细菌繁殖 

math, http://cs101.openjudge.cn/practice/02712

一种细菌的繁殖速度是每天成倍增长。例如：第一天有10个，第二天就变成20个，第三天变成40个，第四天变成80个，……。现在给出第一天的日期和细菌数目，要你写程序求出到某一天的时候，细菌的数目。

**输入**

第一行有一个整数n，表示测试数据的数目。其后n行每行有5个整数，整数之间用一个空格隔开。第一个数表示第一天的月份，第二个数表示第一天的日期，第三个数表示第一天细菌的数目，第四个数表示要求的那一天的月份，第五个数表示要求的那一天的日期。已知第一天和要求的一天在同一年并且该年不是闰年，要求的一天一定在第一天之后。数据保证要求的一天的细菌数目在长整数（long）范围内。

**输出**

对于每一组测试数据，输出一行，该行包含一个整数，为要求的一天的细菌数。

样例输入

```
2
1 1 1 1 2
2 28 10 3 2
```

样例输出

```
2
40
```

来源

2005~2006医学部计算概论期末考试





【宋昕杰，物理学院，2023年秋】

思路：首先将月份天数存储为字典便于计算天数；然后读取输入，计算天数，最后代入指数增长公式计算即可



##### 代码

```python
months = {}
for i in range(12):
    if i + 1 in [1, 3, 5, 7, 8, 10, 12]:
        months[i + 1] = 31
    elif i + 1 == 2:
        months[2] = 28
    else:
        months[i + 1] = 30

n = int(input())
for i in range(n):
    i_month, i_date, num, f_month, f_date = map(int, input().split())
    days = f_date - i_date
    for j in range(i_month, f_month):
        days += months[j]
    print(num*(2**days))
```



代码运行截图 

![image-20231005164156433](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051641563.png)



#### 02753: 菲波那契数列

math, http://cs101.openjudge.cn/practice/02753

菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
给出一个正整数a，要求菲波那契数列中第a个数是多少。
**输入**
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a(1 <= a <= 20)
**输出**
输出有n行，每行输出对应一个输入。输出应是一个正整数，为菲波那契数列中第a个数的大小
样例输入

```
4
5
2
19
1
```

样例输出

```
5
1
4181
1
```





【宋昕杰，物理学院，2023年秋】

思路：记录输入的最大数，计算斐波那契数列至对应项，然后利用列表索引输出即可



##### 代码

```python
inputs = []
outputs = []
n = int(input())

for i in range(n):
    inputs.append(int(input()))

max_index = max(inputs)
for i in range(max_index):
    if i in [0, 1]:
        outputs.append(1)
    else:
        outputs.append(outputs[-1] + outputs[-2])
for i in inputs:
    print(outputs[i - 1])
```



代码运行截图 

![image-20231005164316335](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051643497.png)



#### 02810: 完美立方

bruteforce, http://cs101.openjudge.cn/practice/02810

形如$a^3= b^3 + c^3 + d^3$的等式被称为完美立方等式。例如$12^3= 6^3 + 8^3 + 10^3$ 。编写一个程序，对任给的正整数N (N ≤ 100)，寻找所有的四元组 (a, b, c, d)，使得 $a^3 = b^3 + c^3 + d^3$，其中 a,b,c,d 大于 1, 小于等于N，且 b ≤ c ≤ d。

**输入**

一个正整数N (N≤100)。

**输出**

每行输出一个完美立方。输出格式为：
Cube = a, Triple = (b,c,d)
其中a,b,c,d所在位置分别用实际求出四元组值代入。

请按照a的值，从小到大依次输出。当两个完美立方等式中a的值相同，则b值小的优先输出、仍相同则c值小的优先输出、再相同则d值小的先输出。

样例输入

```
24
```

样例输出

```
Cube = 6, Triple = (3,4,5)
Cube = 12, Triple = (6,8,10)
Cube = 18, Triple = (2,12,16)
Cube = 18, Triple = (9,12,15)
Cube = 19, Triple = (3,10,18)
Cube = 20, Triple = (7,14,17)
Cube = 24, Triple = (12,16,20)
```





【宋昕杰，物理学院，2023年秋】

思路：生成立方数列表，然后遍历b,c,d的所有可能，如果成立，则将a,b,c,d视为ASCII码存储为对应字符串，利用Python的字符串比较对结果进行排序，再转化成数字输出



##### 代码

```python
pairs = []
max_num = 100**3
n = int(input())
nums = [(i + 1)**3 for i in range(1, n)]
for i in range(n - 1):
    for j in range(i, n - 1):
        for k in range(j, n - 1):
            sum_num = nums[i] + nums[j] + nums[k]
            if sum_num in nums:
                pairs.append(f'{chr(nums.index(sum_num) + 2)}{chr(i + 2)}{chr(j + 2)}{chr(k + 2)}')
pairs.sort()
for pair in pairs:
    print(f'Cube = {ord(pair[0])}, Triple = ({ord(pair[1])},{ord(pair[2])},{ord(pair[3])})')
```



代码运行截图 

![image-20231005164521773](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051645063.png)



#### 04138: 质数的和与积

math, http://cs101.openjudge.cn/practice/04138

两个质数的和是S，它们的积最大是多少？

**输入**

一个不大于10000的正整数S，为两个质数的和。

**输出**

一个整数，为两个质数的最大乘积。数据保证有解。

样例输入

```
50
```

样例输出

```
589
```

来源

《奥数典型题举一反三（小学五年级）》 (ISBN 978-7-5445-2882-5) 第三章 第二讲 例1



【宋昕杰，物理学院，2023年秋】

思路：首先找到小于等于s的所有质数，然后从中间开始向两边寻找可行解并相乘输出



##### 代码

```python
s = int(input())
nums = {i: 1 for i in range(2, s)}

for num in nums.keys():
    i = 2
    while i*num < s:
        nums[i*num] = 0
        i += 1

begin = s // 2 + 1
while True:
    if nums[begin] == 1 and nums[s - begin] == 1:
        print(begin*(s - begin))
        break
    begin -= 1
```



代码运行截图 

![image-20231005164645891](C:/Users/m1889/AppData/Roaming/Typora/typora-user-images/image-20231005164645891.png)



#### 04146: 数字方格

math, http://cs101.openjudge.cn/practice/04146

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2747_1.jpg)
如上图，有3个方格，每个方格里面都有一个整数a1，a2，a3。已知0 <= a1, a2, a3 <= n，而且a1 + a2是2的倍数，a2 + a3是3的倍数， a1 + a2 + a3是5的倍数。你的任务是找到一组a1，a2，a3，使得a1 + a2 + a3最大。

输入

一行，包含一个整数n (0 <= n <= 100)。

输出

一个整数，即a1 + a2 + a3的最大值。

样例输入

```
3
```

样例输出

```
5
```





【宋昕杰，物理学院，2023年秋】

思路：暴力求解



##### 代码

```python
n = int(input())
sums = []

for a1 in range(n + 1):
    for a2 in range(n + 1):
        for a3 in range(n + 1):
            if (a1 + a2)%2 == (a2 + a3)%3 == (a1 + a2 + a3)%5 == 0:
                sums.append(a1 + a2 + a3)

print(max(sums))
```



代码运行截图 

![image-20231005164742891](C:/Users/m1889/AppData/Roaming/Typora/typora-user-images/image-20231005164742891.png)



## 2. 选做题目

#### 02746: 约瑟夫问题

implementation, http://cs101.openjudge.cn/practice/02746

约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。

**输入**

每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：

0 0

**输出**

对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号

样例输入

```
6 2
12 4
8 3
0 0
```

样例输出

```
5
1
7
```



【宋昕杰，物理学院，2023年秋】

思路：这题做过不止一次，以往使用模拟法完成题目，这次借助整除算法省去了模拟的时间



##### 代码

```python
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
        
    circle = [i + 1 for i in range(n)]
    pre_index = -1
    index = 0
    for i in range(n - 1):
        index = (m % (n - i) + pre_index) % (n - i)
        pre_index = index - 1
        circle.pop(index)

    print(circle[0])
```



代码运行截图 

![image-20231005164933778](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051649045.png)



#### CF1364A: A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

Ehab loves number theory, but for some reason he hates the number 𝑥. Given an array 𝑎, find the length of its longest subarray such that the sum of its elements **isn't** divisible by 𝑥, or determine that such subarray doesn't exist.

An array 𝑎 is a subarray of an array 𝑏 if 𝑎 can be obtained from 𝑏 by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

The first line contains an integer 𝑡 (1≤𝑡≤5) — the number of test cases you need to solve. The description of the test cases follows.

The first line of each test case contains 2 integers 𝑛 and 𝑥 (1≤𝑛≤10^5^, 1≤𝑥≤10^4^) — the number of elements in the array 𝑎 and the number that Ehab hates.

The second line contains 𝑛 space-separated integers $𝑎_1, 𝑎_2, ……, 𝑎_𝑛 (0≤𝑎_𝑖≤10^4)$ — the elements of the array 𝑎.

**Output**

For each testcase, print the length of the longest subarray whose sum isn't divisible by 𝑥. If there's no such subarray, print −1.

Example

input

```
3
3 3
1 2 3
3 4
1 2 3
2 2
0 6
```

output

```
2
3
-1
```

Note

In the first test case, the subarray \[2,3\] has sum of elements 5, which isn't divisible by 3.

In the second test case, the sum of elements of the whole array is 6, which isn't divisible by 4.

In the third test case, all subarrays have an even sum, so the answer is −1.



【宋昕杰，物理学院，2023年秋】

思路：先判断整个数组是否满足要求，若否则从两侧同时向中间寻找最靠近边缘的不能被x整除的数，将这个数及外侧的数删去即可达到要求



##### 代码

```python
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    array = [int(j) for j in input().split()]
    if sum(array) % x != 0:
        print(n)
    else:
        found = False
        for j in range(n):
            if array[j] % x != 0 or array[n - 1 - j] % x != 0:
                found = True
                break
        if found:
            print(n - j - 1)
        else:
            print(-1)
```



代码运行截图 

![image-20231005165542564](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202310051655901.png)



## 3. 学习总结和收获

​	依然是注意审题，如OJ04146中n可以等于0，CF1364A中子序列的定义是从开头或末尾删去元素得到的序列。

​	国庆前读完了《算法图解》，除了动态规划问题，书中涉及的算法的典型题目应该是可以完成的；本来应该抓紧国庆假期找对应的题目巩固刚学习的算法，并且完成前面的选做题的，但最近重点在CUPT的任务上，所以只是完成了一小部分选做题，等CUPT的任务完成再一边学算法一边刷题。

​	截至2023年10月5日17：00，OJ完成题目58道，CF完成题目26道。





