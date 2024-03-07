"""于2023-12-23测试通过"""
from heapq import heappush, heappop, heapify
from queue import Queue

q = Queue()
left_heap = []
right_heap = []
heapify(left_heap)
heapify(right_heap)
left_dic, right_dic = {}, {}
mid = -float('inf')
num = 0
ans = ''


def left(t):
    if t in left_dic:
        left_dic[t] += 1
    else:
        left_dic[t] = 1


def right(t):
    if t in right_dic:
        right_dic[t] += 1
    else:
        right_dic[t] = 1


def left_adjust():
    global t
    while len(left_heap):
        t = -heappop(left_heap)
        if left_dic[t]:
            heappush(left_heap, -t)
            break


def right_adjust():
    global t
    while len(right_heap):
        t = heappop(right_heap)
        if right_dic[t]:
            heappush(right_heap, t)
            break


for _ in range(int(input())):
    s = input()
    if s == 'del':
        t = q.get()
        if t >= mid:
            right_dic[t] -= 1
            if num % 2 == 0:
                t = -heappop(left_heap)
                left_dic[t] -= 1
                right(t)
                heappush(right_heap, t)
                mid = t
            else:
                right_adjust()
                left_adjust()
                if len(right_heap):
                    l, r = -heappop(left_heap), heappop(right_heap)
                    mid = (l + r)/2
                    heappush(left_heap, -l)
                    heappush(right_heap, r)
                else:
                    mid = -float('inf')
        else:
            left_dic[t] -= 1
            if num % 2 == 0:
                left_adjust()
                mid = heappop(right_heap)
                heappush(right_heap, mid)
            else:
                t = heappop(right_heap)
                right_dic[t] -= 1
                left(t)
                mid = t
                heappush(left_heap, -t)
                right_adjust()
                mid = (mid + t) / 2
        num -= 1
    elif s == 'query':
        ans += str(int(mid) if mid == int(mid) else mid) + '\n'
    else:
        t = int(s.split()[1])
        q.put(t)
        if num % 2 == 1:
            if t >= mid:
                right(t)
                heappush(right_heap, t)
                t = heappop(right_heap)
                right_dic[t] -= 1
                left(t)
                heappush(left_heap, -t)
                right_adjust()
            else:
                left(t)
                heappush(left_heap, -t)
                left_adjust()
            mid = (mid + t)/2
        else:
            if t >= mid:
                right(t)
                heappush(right_heap, t)
                t = heappop(right_heap)
                heappush(right_heap, t)
            else:
                left(t)
                heappush(left_heap, -t)
                t = -heappop(left_heap)
                left_dic[t] -= 1
                right(t)
                heappush(right_heap, t)
            mid = t
        num += 1
print(ans)