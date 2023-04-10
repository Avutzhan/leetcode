import unittest

from Practice.search import linear_search, binary_search


class TestSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3], 5), -1)
        self.assertEqual(linear_search([1, 2, 3], 3), 2)

    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3], 5), -1)
        self.assertEqual(binary_search([1, 2, 3], 3), 2)


if __name__ == '__main__':
    unittest.main()
