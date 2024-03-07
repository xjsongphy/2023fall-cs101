""""于2023-8-31测试通过"""
print('+'.join([str(i) for i in sorted([int(i) for i in input().split('+')])]))