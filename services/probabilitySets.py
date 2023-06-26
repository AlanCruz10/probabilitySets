import itertools
from fractions import Fraction

def print_result(x):
    print(f'[{Fraction(x).limit_denominator()}, {round(x, 4)}]]')

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_fibonacci_probability(quantity, numbers):
    total_combinations = numbers ** quantity
    fibonacci_sums = 0

    for i in range(1, quantity * numbers + 1):
        if i in [fibonacci(n) for n in range(1, 12)]:
            fibonacci_sums += 1

    fibonacci_probability = fibonacci_sums / total_combinations
    print_result(fibonacci_probability)
    return fibonacci_probability

def calculate_probability_odd(quantity, numbers):
    total_outcomes = numbers ** quantity
    odd_sum_outcomes = 0

    for outcome in itertools.product(range(1, numbers + 1), repeat=quantity):
        if sum(outcome) % 2 != 0:
            odd_sum_outcomes += 1

    probability = odd_sum_outcomes / total_outcomes
    print_result(probability)
    return probability

def calculate_probability_even(quantity, numbers):
    total_outcomes = numbers ** quantity
    even_sum_outcomes = 0

    for outcome in itertools.product(range(1, numbers + 1), repeat=quantity):
        if sum(outcome) % 2 != 0:
            even_sum_outcomes += 1

    probability = even_sum_outcomes / total_outcomes
    print_result(probability)
    return probability

def calculate_prime_probability(quantity, numbers):
    total_outcomes = numbers ** quantity
    prime_outcomes = 0

    outcomes = itertools.product(range(1, numbers + 1), repeat=quantity)

    for outcome in outcomes:
        if is_prime(sum(outcome)):
            prime_outcomes += 1

    prime_probability = prime_outcomes / total_outcomes
    print_result(prime_probability)
    return prime_probability

def greater_than_number_probability(quantity, numbers, y):
    total_outcomes = numbers**quantity
    favorable_outcomes = 0

    outcomes = itertools.product(range(1, numbers + 1), repeat=quantity)

    for outcome in outcomes:
        if sum(outcome) > y:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    print_result(probability)
    return probability

def probability_less_than_number(quantity, numbers, y):
    total_outcomes = numbers**quantity
    favorable_outcomes = 0

    outcomes = itertools.product(range(1, numbers + 1), repeat=quantity)

    for outcome in outcomes:
        if sum(outcome) < y:
            favorable_outcomes += 1

    probability = favorable_outcomes / total_outcomes
    print_result(probability)
    return probability

calculate_fibonacci_probability(1,6)
calculate_probability_odd(2, 6)
calculate_probability_even(2, 6)
calculate_prime_probability(2,6)
greater_than_number_probability(1,6, 5)
probability_less_than_number(1,6, 5)