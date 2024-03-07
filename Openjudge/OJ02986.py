from math import factorial

try:
    while True:
        input_str = input()
        str_list = input_str.split()

        n = int(str_list[0])
        k = int(str_list[1])

        C_n_k = factorial(n) / (factorial(n - k) * factorial(k))

        print(int(C_n_k % 2))
except EOFError:
    pass