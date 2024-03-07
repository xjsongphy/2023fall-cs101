# 计算概论(B) 课前问题4

Updated 1524 GMT+8 Sep 2, 2023



2023 fall, Complied by Hongfei Yan

Markdown（用 https://typoraio.cn 编辑）格式文件在，https://github.com/GMyhf/2023fall-cs101

## Answer:

【宋昕杰，物理学院，2023年秋】

操作系统：Windows 11 22H2

Python编程环境：PyCharm 2023.1.3 (Community Edition)

C/C++编程环境：g++ (x86_64-win32-seh-rev0, Built by MinGW-W64 project) 8.1.0



思路：

找到1的位置，根据这个位置计算距离中心的步数



### Python3 代码

```python
index = None

for i in range(5):          #读取输入，找到1的位置
    input_list = input().split()
    for j in range(5):
        if input_list[j] == '1':
            index = (i, j)
            break

print(abs(index[0] - 2) + abs(index[1] - 2))
```

Python代码运行截图

![image-20230904163044787](C:\Users\m1889\AppData\Roaming\Typora\typora-user-images\image-20230904163044787.png)



### C++ 代码

```c++
#include<iostream>
using namespace std;

int main()
{
    int iIndexOfX, iIndexOfY;
    char cTemp;

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            cin >> cTemp;
            if(cTemp == '1')
            {
                iIndexOfX = i;
                iIndexOfY = j;
                break;
            }
        }
    }

    cout << abs(2 - iIndexOfX) + abs(2 - iIndexOfY);
    return 0;
}
```

C++ 代码运行截图

![image-20230905210240285](C:\Users\m1889\AppData\Roaming\Typora\typora-user-images\image-20230905210240285.png)

## 4. 学习总结和收获

此题不必存储所有数据，直接在读取时完成判断即可；从运行时间和代码上可以看出C++的高效和Python的简洁