import sys
import numpy as np


def calculate_cost(numbers: [int]) -> int:
    cost = 0
    numbers = np.array(numbers)

    for i in range(numbers.shape[0] - 1):
        j = i

        while numbers[j] != (i + 1):
            j += 1

        cost += j - i + 1
        numbers = np.concatenate((numbers[:i], numbers[i:j+1][::-1], numbers[j+1:]))

    return cost


if __name__ == "__main__":
    n_test_cases = int(sys.stdin.readline())

    for i in range(n_test_cases):
        n_numbers = int(sys.stdin.readline())
        input_numbers = sys.stdin.readline()
        input_numbers = input_numbers.split(" ")
        input_numbers = [int(j) for j in input_numbers]
        print(f"Case #{i + 1}: {calculate_cost(input_numbers)}")
