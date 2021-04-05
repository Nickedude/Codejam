import unittest
import random
from reversort import calculate_cost


class TestGenerateList(unittest.TestCase):

    def test_reversort_example_1(self):
        self.assertEqual(6, calculate_cost([4, 2, 1, 3]))

    def test_reversort_example_2(self):
        self.assertEqual(1, calculate_cost([1, 2]))

    def test_reversort_example_3(self):
        self.assertEqual(12, calculate_cost([7, 6, 5, 4, 3, 2, 1]))

    def test_reversort_random_sorted_is_zero(self):
        random.seed(0)

        for i in range(2, 100):
            xs = list(range(1, i))
            self.assertEqual(len(xs) - 1, calculate_cost(xs))

if __name__ == "__main__":
    unittest.main()