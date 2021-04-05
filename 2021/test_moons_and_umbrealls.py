import unittest
from moons_and_umbrellas import mural_cost

class TestMuralCost(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(5, mural_cost(2, 3, "CJ?CC?"))

    def test_example_two(self):
        self.assertEqual(10, mural_cost(4, 2, "CJCJ"))

    def test_example_three(self):
        self.assertEqual(1, mural_cost(1, 3, "C?J"))

    def test_example_four(self):
        self.assertEqual(0, mural_cost(2, 5, "??J???"))