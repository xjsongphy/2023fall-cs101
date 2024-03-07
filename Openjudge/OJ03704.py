"""于2023-11-1测试通过"""
from queue import LifoQueue
try:
    while True:
        stack = LifoQueue()
        data = input()
        print(data)
        ans = [' ']*len(data)
        for i in range(len(data)):
            if data[i] == '(':
                stack.put(i)
            elif data[i] == ')':
                if stack.empty():
                    ans[i] = '?'
                else:
                    ans[stack.get()] = ' '
                    ans[i] = ' '
            else:
                ans[i] = ' '
        for i in range(stack.qsize()):
            ans[stack.get()] = '$'
        print(''.join(ans))
except:
    pass