import unittest

from Practice.sort import quick_sort


class TestSort(unittest.TestCase):

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([3, 2, 1, 0, -1, -11]), [-11, -1, 0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
