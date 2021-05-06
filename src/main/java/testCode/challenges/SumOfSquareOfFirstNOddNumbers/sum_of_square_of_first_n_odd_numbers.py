def sum_of_square_of_first_n_odd_numbers(input: int) -> int:
    return sum([x**2 for x in range(1, input*2+1, 2) if x % 2 == 1])
