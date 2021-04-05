import sys
from copy import deepcopy

import numpy as np


_memory = {}


def _memoize(size: int, cost: int, solution: np.ndarray):
    if (size, cost) not in _memory:
        _memory[(size, cost)] = deepcopy(solution)


def generate_list(size, cost) -> list:
    solution = generate_list_helper(size, cost)

    if solution is None:
        raise ValueError("Failed to find solution!")

    return list(solution.astype(int))


def generate_list_helper(size, cost) -> np.ndarray:
    if (size, cost) in _memory:
        return deepcopy(_memory[(size, cost)])

    max_cost = size * (size + 1) / 2 - 1
    min_cost = size - 1

    if cost < min_cost or cost > max_cost:
        solution = None
        _memoize(size, cost, solution)
        return solution

    if size == 1:
        return np.array([1])

    for i in range(size):
        solution = generate_list_helper(size - 1, cost - 1 - i)

        if solution is None:
            continue

        solution += 1
        solution = np.concatenate((np.ones(1), solution))

        to_reverse = solution[:i+1]
        to_reverse = to_reverse[::-1]

        solution = np.concatenate((to_reverse, solution[i+1:]))
        _memoize(size, cost, solution)
        return solution

    _memoize(size, cost, None)
    return None


if __name__ == "__main__":
    n_test_cases = int(sys.stdin.readline())

    for i in range(n_test_cases):
        input_numbers = sys.stdin.readline()
        input_numbers = input_numbers.split(" ")
        input_size, input_cost = int(input_numbers[0]), int(input_numbers[1])
        solution = ""
        try:
            solution = generate_list(input_size, input_cost)
            solution = list(map(str, solution))
            solution = " ".join(solution)
        except ValueError:
            solution = "IMPOSSIBLE"
        finally:
            print(f"Case #{i + 1}: {solution}")
