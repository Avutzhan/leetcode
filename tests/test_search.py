import unittest

from Practice.search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(linear_search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_binary_search(self):
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(binary_search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == '__main__':
    unittest.main()
