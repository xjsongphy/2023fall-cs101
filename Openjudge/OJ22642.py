"""于2023-9-21测试通过"""
possible_solutions = []
n = int(input())


def main_func(single_pairs, possible_solution):
    if len(possible_solution) == 2*n and single_pairs == 0:
        possible_solutions.append(possible_solution)
    elif len(possible_solution) < 2*n:
        if single_pairs > 0:
            main_func(single_pairs - 1, possible_solution + ')')
        if single_pairs < n:
            main_func(single_pairs + 1, possible_solution + '(')


main_func(1, '(')
for possible_solution in sorted(possible_solutions):
    print(possible_solution)
