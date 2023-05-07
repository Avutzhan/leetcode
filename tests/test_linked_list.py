import unittest

from Practice.linked_list import LinkedList


class TestSearch(unittest.TestCase):

    def test_get_head(self):
        lst = LinkedList()
        self.assertEqual(lst.get_head(), None)

    def test_is_empty(self):
        lst = LinkedList()
        self.assertEqual(lst.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
