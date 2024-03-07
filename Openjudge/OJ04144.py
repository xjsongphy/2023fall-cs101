"""于2023-11-3测试通过"""
import heapq as h

n = int(input())
cows = sorted([list(map(int, input().split())) + [i + 1] for i in range(n)], key=lambda t: t[0])
nte = {}
etn = {}
heap = []
total = 0
h.heapify(heap)
for cow in cows:
    is_in = False
    if len(heap):
        end = h.heappop(heap)
        if end < cow[0]:
            num = etn[end].pop()
            cow[0] = num
            nte[num] = cow[1]
            if etn.get(cow[1]):
                etn[cow[1]].append(num)
            else:
                etn[cow[1]] = [num]
            is_in = True
            h.heappush(heap, cow[1])
        else:
            h.heappush(heap, end)
    if not is_in:
        total += 1
        h.heappush(heap, cow[1])
        nte[total] = cow[1]
        if etn.get(cow[1]):
            etn[cow[1]].append(total)
        else:
            etn[cow[1]] = [total]
        cow[0] = total
print(total)
cows.sort(key=lambda t: t[2])
for cow in cows:
    print(cow[0])