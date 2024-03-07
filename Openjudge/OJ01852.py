"""于2023-9-27测试通过"""
#下方为较短代码
n = int(input())
for i in range(n):
    l, k = map(int, input().split())
    ds, left, right = [int(j) for j in input().split()], [], []
    for d in ds:
        [right, left][d < l/2].append(d)
    if left and right:
        print(max(max(left), l - min(right)), max(l - min(left), max(right)))
    elif left and not right:
        print(max(left), l - min(left))
    else:
        print(l - min(right), max(right))

#下方为较快代码
# n = int(input())
# for i in range(n):
#     l, k = map(int, input().split())
#     locations = list(map(int, input().split()))
#     left_ants = []
#     right_ants = []
#     for location in locations:
#         if location < l / 2:
#             left_ants.append(location)
#         else:
#             right_ants.append(location)
#     if not left_ants and right_ants:
#         print(f'{l - min(right_ants)} {max(right_ants)}')
#     elif left_ants and not right_ants:
#         print(f'{max(left_ants)} {l - min(left_ants)}')
#     else:
#         print(f'{max(max(left_ants), l - min(right_ants))} {max(l - min(left_ants), max(right_ants))}')