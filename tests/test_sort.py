import unittest

from Practice.sort import quick_sort, merge_sort, merge


class TestSort(unittest.TestCase):

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([3, 2, 1, 0, -1, -11]), [-11, -1, 0, 1, 2, 3])

    def test_merge(self):
        self.assertEqual(merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([], []), [])
        self.assertEqual(merge([-11, -1, 0], [1, 2, 3]), [-11, -1, 0, 1, 2, 3])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([1, 5, 6, 9, 11, 3, 4, 7, 8, 10]), [1, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge_sort([3, 2, 1, 0, -1, -11]), [-11, -1, 0, 1, 2, 3])
        self.assertEqual(merge_sort([]), [])


if __name__ == '__main__':
    unittest.main()