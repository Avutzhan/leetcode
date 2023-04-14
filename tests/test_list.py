import unittest

from Practice.lists import remove_even, find_sum, find_product, find_minimum, find_unique


class TestSearch(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(remove_even([-1, 0, 3, 5, 9, 12]), [-1, 3, 5, 9])

    def test_find_sum(self):
        self.assertEqual(find_sum([1, 2, 3, 4], 5), [1, 4])

    def test_find_product(self):
        self.assertEqual(find_product([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_find_minimum(self):
        self.assertEqual(find_minimum([1, 2, 3, 4]), 1)

    def test_find_unique(self):
        self.assertEqual(find_unique([1, 1, 2, 3, 3, 4, 4]), 2)


if __name__ == '__main__':
    unittest.main()
