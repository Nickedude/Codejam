import unittest

from tqdm import tqdm

from reversort_engineering import generate_list
from reversort import calculate_cost


class TestReversortEngineering(unittest.TestCase):

    def test_generate_list_example_one(self):
        l = generate_list(4, 6)
        self.assertEqual(6, calculate_cost(l))

    def test_generate_list_example_two(self):
        self.assertEqual(2, calculate_cost(generate_list(2, 2)))

    def test_generate_list_example_three(self):
        self.assertEqual(12, calculate_cost(generate_list(7, 12)))

    def test_generate_list_too_low_cost(self):
        for i in range(2, 100):
            with self.assertRaises(ValueError):
                generate_list(size=i, cost=i-2)

    def test_generate_list_too_high_cost(self):
        for i in range(2, 100):
            with self.assertRaises(ValueError):
                generate_list(size=i, cost=i * (i + 1) / 2)

    def test_min_cost(self):
        for i in range(2, 100):
            expected = [j for j in range(1, i + 1)]
            self.assertEqual(expected, generate_list(i, i - 1))

    def test_size_two(self):
        _test_generate_for_size(2, 1, 2)

    def test_size_three(self):
        _test_generate_for_size(3, 2, 4)

    def test_size_four(self):
        _test_generate_for_size(4, 3, 7)

    def test_size_five(self):
        _test_generate_for_size(5, 4, 10)

    def test_size_seven(self):
        _test_generate_for_size(7, 6, 18)

    def test_size_nine(self):
        _test_generate_for_size(9, 8, 28)

    def test_all(self):
        for i in tqdm(range(2, 100)):
            for j in range(1, i - 1):
                with self.assertRaises(ValueError):
                    generate_list(i, j)

            max_cost = int(i * (i + 1) / 2 - 1)
            _test_generate_for_size(i, i - 1, max_cost)

            for j in range(max_cost + 1, 1000):
                with self.assertRaises(ValueError):
                    generate_list(i, j)


def _test_generate_for_size(size, min_cost, max_cost):
    for cost in range(min_cost, max_cost + 1):
        l = generate_list(size, cost)
        assert size == len(l)
        assert cost == calculate_cost(l)

        expected = set(list(range(1, size + 1)))
        actual = set(l)
        assert actual == expected, f"{expected} \n {actual}"

