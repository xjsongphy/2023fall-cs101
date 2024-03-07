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