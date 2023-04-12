import unittest

from Practice.lists import remove_even, find_sum


class TestSearch(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(remove_even([-1, 0, 3, 5, 9, 12]), [-1, 3, 5, 9])

    def test_find_sum(self):
        self.assertEqual(find_sum([1, 2, 3, 4], 5), [1, 4])


if __name__ == '__main__':
    unittest.main()
