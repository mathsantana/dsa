import unittest
from linkedlist import LinkedList

class TestLinkedListMethods(unittest.TestCase):
    def test_linked_list_constructor(self):
        lst = LinkedList()
        self.assertTrue(lst.isEmpty())

    def test_linked_list_addFirst(self):
        values = [1,2,3]
        lst = LinkedList()

        reversed_values = values.copy()
        reversed_values.reverse()

        for v in reversed_values:
            lst.addFirst(v)

        for v in values:
            self.assertEqual(v, lst.pop())
        self.assertTrue(lst.isEmpty())

    def test_linked_list_addLast(self):
        values = [1,2,3]
        lst = LinkedList()

        for v in values:
            lst.addLast(v)

        for v in values:
            self.assertEqual(v, lst.pop())

        self.assertTrue(lst.isEmpty())

    def test_linked_list_pop(self):
        lst = LinkedList()
        with self.assertRaises(ReferenceError):
            lst.pop()

        lst.addLast(1)

        self.assertEqual(1, lst.pop())

        lst.addLast(2)
        lst.addLast(3)

        self.assertEqual(2, lst.pop())


if __name__ == '__main__':
    unittest.main()
