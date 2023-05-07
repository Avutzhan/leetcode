import unittest

from Practice.list import remove_even, find_sum, find_product, find_minimum, find_unique, find_second_maximum, \
    right_rotate, rearrange, max_min, find_max_sum_sublist


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

    def test_find_second_maximum(self):
        self.assertEqual(find_second_maximum([9, 2, 3, 6]), 6)
        self.assertEqual(find_second_maximum([4, 2, 1, 5, 0]), 4)

    def test_right_rotate(self):
        self.assertEqual(right_rotate([], 1), [])
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(right_rotate([300, -1, 3, 0], 3), [-1, 3, 0, 300])
        self.assertEqual(right_rotate([0, 0, 0, 2], 2), [0, 2, 0, 0])
        self.assertEqual(right_rotate(['13', 'a', 'Python'], 3), ['13', 'a', 'Python'])

    def test_rearrange(self):
        self.assertEqual(rearrange([-1, 2, -3, -4, 5]), [-1, -3, -4, 2, 5])
        self.assertEqual(rearrange([300, -1, 3, 0]), [-1, 300, 3, 0])
        self.assertEqual(rearrange([0, 0, 0, -2]), [-2, 0, 0, 0])

    def test_max_min(self):
        self.assertEqual(max_min([1, 2, 3, 4, 5, 6, 7]), [7, 1, 6, 2, 5, 3, 4])
        self.assertEqual(max_min([1, 2, 3, 4, 5]), [5, 1, 4, 2, 3])
        self.assertEqual(max_min([]), [])
        self.assertEqual(max_min([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(max_min([-10, -1, 1, 1, 1, 1]), [1, -10, 1, -1, 1, 1])

    def test_find_max_sum_sublist(self):
        self.assertEqual(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]), 12)


if __name__ == '__main__':
    unittest.main()
