"""于2023-8-26测试通过"""
# 于2023-10-26改进
def main(ls):
    if ls[1] % ls[0]:
        main(sorted([ls[0], ls[1] - ls[0]]))
    else:
        print(ls[0])


try:
    while True:
        main(sorted(list(map(int, input().split()))))
except EOFError:
    pass
