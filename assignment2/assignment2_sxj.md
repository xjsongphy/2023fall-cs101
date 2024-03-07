# Assignment #2: 字符串相关

Updated 0014 GMT+8 Sep 20, 2023



2023 fall, Complied by Xinjie Song, Phy



**说明：**

1）第2周课上讲到了计算机相关的历史，介绍了ASCII表。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）同学完成作业的时候，就是这个模版文件中修改补充好。为便于助教批改作业，请尽量不要删除其他文字。

5）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows 11 22H2 

Python编程环境：PyCharm 2023.2 (Community Edition) 

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0 



## 1. 必做题目

#### 71A. Way Too Long Words

strings, 1000, http://codeforces.com/problemset/problem/71/A

Sometimes some words like "*localization*" or "*internationalization*" are so long that writing them many times in one text is quite tiresome.

Let's consider a word *too long*, if its length is **strictly more** than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "*localization*" will be spelt as "*l10n*", and "*internationalization*" will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

**Input**

The first line contains an integer *n* (1 ≤ *n* ≤ 100). Each of the following *n* lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

**Output**

Print *n* lines. The *i*-th line should contain the result of replacing of the *i*-th word from the input data.

Examples

input

```
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```

output

```
word
l10n
i18n
p43s
```



【宋昕杰，物理学院，2023年秋】

思路：利用Python丰富的builtin函数，调用len()判断字符串的长度，以及索引0和-1分别获取首位字符，通过字符串的加减完成对字符串的编辑



##### Python3 代码

```python
n = int(input())

for i in range(0, n):
    str_input = input()
    if len(str_input) > 10:
        print(str_input[0] + str(len(str_input) - 2) + str_input[-1])
    else:
        print(str_input)
```



Python代码运行截图 

![image-20230921180643052](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211806335.png)





C++ 代码

```c++
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int n;
    string input;

    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> input;
        if(input.length() > 10)
        {
            cout << input[0] << input.length() - 2 << input[input.length() - 1];

        }
        else
        {
            cout << input;
        }
        cout << endl;
    }

    return 0;
}
```



C++ 代码运行截图 

![image-20230921182803901](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211828051.png)





#### 112A. Petya and Strings

implementation/strings, 800, http://codeforces.com/problemset/problem/112/A

Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

**Input**

Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

**Output**

If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

Examples

input

```
aaaa
aaaA
```

output

```
0
```

input

```
abs
Abz
```

output

```
-1
```

input

```
abcdefg
AbCdEfF
```

output

```
1
```

Note

If you want more formal information about the lexicographical order (also known as the "dictionary order" or "alphabetical order"), you can visit the following site:

- http://en.wikipedia.org/wiki/Lexicographical_order



【宋昕杰，物理学院，2023年秋】

思路：直接利用字符串的默认比较即可



##### Python3 代码

```python
str1, str2 = input().lower(), input().lower()

if str1 > str2:
    print(1)
elif str1 == str2:
    print(0)
else:
    print('-1')
```



Python代码运行截图

![image-20230921180836954](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211808100.png)



C++ 代码

```c++
#include<iostream>
#include<string.h>
using namespace std;
string lower(string);
int main()
{
    string str1, str2;
    cin >> str1 >> str2;

    str1 = lower(str1);
    str2 = lower(str2);
    if(str1 > str2)
    {
        cout << 1;
    }
    else if(str1 == str2)
    {
        cout << 0;
    }
    else
    {
        cout << -1;
    }
    return 0;
}

string lower(string str)
{
    int length = str.length();
    for(int i = 0; i < length; i++)
    {
        if(65 <= int(str[i]) and int(str[i]) <=92)
        {
            str[i] = char(str[i] + 32);
        }
    }
    return str;
}
```



C++ 代码运行截图

![image-20230921184314356](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211843495.png)



#### 158A. Next Round

*special problem/implementation, 800, http://codeforces.com/problemset/problem/158/A

"Contestant who earns a score equal to or greater than the *k*-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of *n* participants took part in the contest (*n* ≥ *k*), and you already know their scores. Calculate how many participants will advance to the next round.

**Input**

The first line of the input contains two integers *n* and *k* (1 ≤ *k* ≤ *n* ≤ 50) separated by a single space.

The second line contains *n* space-separated integers *a*~1~, *a*~2~, ..., a~n~ (0 ≤ a~i~ ≤ 100), where a~i~ is the score earned by the participant who got the *i*-th place. The given sequence is non-increasing (that is, for all *i* from 1 to *n* - 1 the following condition is fulfilled: a~i~ ≥ a~i~ + 1).

**Output**

Output the number of participants who advance to the next round.

Examples

input

```
8 5
10 9 8 7 7 7 5 5
```

output

```
6
```

input

```
4 2
0 0 0 0
```

output

```
0
```

Note

In the first example the participant on the 5th place earned 7 points. As the participant on the 6th place also earned 7 points, there are 6 advancers.

In the second example nobody got a positive score.



【宋昕杰，物理学院，2023年秋】

思路：读取数据，按要求比较并计数，不符合要求则退出循环



##### Python3 代码

```python
input_list = input().split()
n = int(input_list[0])
k = int(input_list[1])

score_list = [int(x) for x in input().split()]

total = 0
for score in score_list:
    if score >= score_list[k - 1] and score > 0:
        total += 1
    else:
        break

print(total)
```



Python代码运行截图 

![image-20230921181128588](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211811737.png)



C++ 代码

```c++
#include<iostream>
using namespace std;
int main()
{
    int n, k, total;
    cin >> n >> k;

    total = 0;
    int score[n];
    for(int i = 0; i < n; i++)
    {
        cin >> score[i];
    }
    for(int i = 0; i < n; i++)
    {
        if(score[i] >= score[k - 1] and score[i] > 0)
        {
            total++;
        }
        else
        {
            break;
        }
    }

    cout << total;
    return 0;
}
```



C++ 代码运行截图

![image-20230921184915418](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211849560.png)





#### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word *s*. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word *s*.

**Input**

The first and only line contains the word *s*, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

**Output**

If Vasya managed to say hello, print "YES", otherwise print "NO".

Examples

input

```
ahhellllloou
```

output

```
YES
```

input

```
hlelo
```

output

```
NO
```





【宋昕杰，物理学院，2023年秋】

思路：利用str类中的find()方法返回带查找字符第一次出现的索引这一特性，在输入字符串中依次查找'hello'中的每一个字符，并在查找后删去输入字符串无用的部分



##### Python3 代码

```python
str_input = input()
str_wanted = 'hello'
yes_or_no = True

for i in range(0, len(str_wanted)):
    if str_wanted[i] in str_input:
        index = str_input.find(str_wanted[i])

        if index == len(str_input) - 1:
            str_input = ''
        else:
            str_input = str_input[index + 1:]
    else:
        yes_or_no = False
        break

if yes_or_no:
    print('YES')
else:
    print('NO')
```



Python代码运行截图

![image-20230921181348157](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211813302.png)



C++ 代码

```c++
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    string input, wanted;
    bool success = true;
    wanted = "hello";
    cin >> input;
    
    int index = 0;
    for(int i = 0; i < 5; i++)
    {
        bool exist = false;
        for(; index < input.length(); index++)
        {
            if(input[index] == wanted[i])
            {
                index++;
                exist = true;
                break;
            }
        }
        if(not exist)
        {
            success = false;
            break;
        }
    }

    if(success)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}
```



C++ 代码运行截图

![image-20230921185644150](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211856297.png)





#### 04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015

POJ 注册的时候需要用户输入邮箱，验证邮箱的规则包括：
1)有且仅有一个'@'符号
2)'@'和'.'不能出现在字符串的首和尾
3)'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连
满足以上3条的字符串为合法邮箱，否则不合法，
编写程序验证输入是否合法

**输入**

输入包含若干行，每一行为一个代验证的邮箱地址，长度小于100

**输出**

每一行输入对应一行输出
如果验证合法，输出 YES
如果验证非法：输出 NO

样例输入

```
.a@b.com
pku@edu.cn
cs101@gmail.com
cs101@gmail
```

样例输出

```
NO
YES
YES
NO
```





【宋昕杰，物理学院，2023年秋】

思路：使用if和elif依次排除即可，注意'.'在'@'前的情况，第一次提交时并没有注意到



##### Python3 代码

```python
while True:
    try:
        str_input = input()

        if str_input.count('@') != 1:
            print('NO')
        elif str_input[0] == '@' or str_input[0] == '.':
            print('NO')
        elif str_input[-1] == '@' or str_input[-1] == '.':
            print('NO')
        else:
            at_index = str_input.index('@')
            if str_input[at_index:].count('.') == 0:
                print('NO')
            elif str_input[at_index + 1] == '.' or str_input[at_index - 1] == '.':
                print('NO')
            else:
                print('YES')
    except EOFError:
        break
```



Python代码运行截图

![image-20230921181829451](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211818707.png)



## 2. 选做题目

#### OJ01008: Maya Calendar

math, http://cs101.openjudge.cn/practice/01008/

During his last sabbatical, professor M. A. Ya made a surprising discovery about the old Maya calendar. From an old knotted message, professor discovered that the Maya civilization used a 365 day long year, called Haab, which had 19 months. Each of the first 18 months was 20 days long, and the names of the months were pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu. Instead of having names, the days of the months were denoted by numbers starting from 0 to 19. The last month of Haab was called uayet and had 5 days denoted by numbers 0, 1, 2, 3, 4. The Maya believed that this month was unlucky, the court of justice was not in session, the trade stopped, people did not even sweep the floor. For religious purposes, the Maya used another calendar in which the year was called Tzolkin (holly year). The year was divided into thirteen periods, each 20 days long. Each day was denoted by a pair consisting of a number and the name of the day. They used 20 names: imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau and 13 numbers; both in cycles. Notice that each day has an unambiguous description. For example, at the beginning of the year the days were described as follows: 1 imix, 2 ik, 3 akbal, 4 kan, 5 chicchan, 6 cimi, 7 manik, 8 lamat, 9 muluk, 10 ok, 11 chuen, 12 eb, 13 ben, 1 ix, 2 mem, 3 cib, 4 caban, 5 eznab, 6 canac, 7 ahau, and again in the next period 8 imix, 9 ik, 10 akbal . . . Years (both Haab and Tzolkin) were denoted by numbers 0, 1, . . . , where the number 0 was the beginning of the world. Thus, the first day was: Haab: 0. pop 0 Tzolkin: 1 imix 0 Help professor M. A. Ya and write a program for him to convert the dates from the Haab calendar to the Tzolkin calendar. 

**输入**

The date in Haab is given in the following format:
NumberOfTheDay. Month Year

The first line of the input file contains the number of the input dates in the file. The next n lines contain n dates in the Haab calendar format, each in separate line. The year is smaller then 5000.

**输出**

The date in Tzolkin should be in the following format:
Number NameOfTheDay Year

The first line of the output file contains the number of the output dates. In the next n lines, there are dates in the Tzolkin calendar format, in the order corresponding to the input dates.

样例输入

```
3
10. zac 0
0. pop 0
10. zac 1995
```

样例输出

```
3
3 chuen 0
1 imix 0
9 cimi 2801
```

来源

Central Europe 1995



【宋昕杰，物理学院，2023年秋】

思路：创建名称列表，首先计算总天数，再分别整除、取余，==最后注意首先将n输出==



##### Python3 代码

```python
n = int(input())
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']

print(n)
for i in range(n):
    num, month, year = map(str, input().split())
    num = int(num.rstrip('.'))
    year = int(year)
    days = num + year*365 + haab.index(month)*20
    year = days//260
    num = (days % 260) % 13
    name = (days % 260) % 20

    print(str(num + 1) + ' ' + tzolkin[name] + ' ' + str(year))
```



Python代码运行截图

![image-20230921193715119](https://raw.githubusercontent.com/xjsongphy/repository_for_typora/main/img/202309211937357.png)



## 3. 学习总结和收获

​	前5题在开学前已经提前完成了，属于基础题目；完成作业时补充了大部分题目的C++代码，感受到Python中诸多特性以及内置函数的便捷性；完成选做题玛雅日历时，深切体会到了审题的重要性：看似无关紧要的n也需要输出，这是我第一次遇到的。

​	9月20日因故未能完成新加入的题目，9月21日恰好完成了两道简单题，也算弥补上了。





