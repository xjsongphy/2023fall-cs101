"""于2023-10-13测试通过"""
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


