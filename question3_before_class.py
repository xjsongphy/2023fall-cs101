"""
Q: Print all prime numbers less than or equal to N
Given a number N, the task is to print all prime numbers less than or equal to N.
"""

prime_numbers = None

try:
    N = int(input())

    if N >= 2:
        prime_numbers = [x for x in range(2, N + 1)]
        i = 0
        while i < len(prime_numbers):
            """递归法删除数据"""
            i += 1

        output_list = ''
        for prime_number in prime_numbers:
            output_list += str(prime_number) + ' '
        output_list.rstrip()
        print(output_list)
    elif N == 1:
        print('NULL')
    else:
        print('ERROR')
except ValueError:
    print('INVALID INPUT')