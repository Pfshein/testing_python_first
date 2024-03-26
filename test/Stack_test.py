from unittest import TestCase, main
from stack.main import Stack


class TestStack(TestCase):

    def test_push_append_one_item(self):
        test_stack = Stack()
        test_stack.push(5)
        self.assertEqual(test_stack.items, [5])

    def test_push_append_and_delite_item(self):
        test_stack = Stack()
        test_stack.push(10)
        test_stack.push('Billy')
        test_stack.pop()
        self.assertEqual(test_stack.size(), 1)

    def test_pop_delite_two_item(self):
        test_stack = Stack()
        test_stack.push(10)
        test_stack.push('Billy')
        test_stack.push('Van')
        test_stack.pop()
        test_stack.pop()
        self.assertEqual(test_stack.items, [10])

    def test_pop_delite_in_empty_list(self):
        with self.assertRaises(IndexError):
            test_stack = Stack()
            test_stack.pop()

    def test_is_empty_on_nonempty_list(self):
        test_stack = Stack()
        test_stack.push(5)
        self.assertEqual(test_stack.is_empty(), False)

    def test_is_empty_on_empty_list(self):
        test_stack = Stack()
        test_stack.push(5)
        test_stack.pop()
        self.assertEqual(test_stack.is_empty(), True)

    def test_size_on_nonempty_list(self):
        test_stack = Stack()
        test_stack.push(5)
        test_stack.push(4)
        test_stack.push(3)
        test_stack.push(1)
        self.assertEqual(test_stack.size(), 4)

    def test_size_on_empty_list(self):
        test_stack = Stack()
        test_stack.push(5)
        test_stack.pop()
        self.assertEqual(test_stack.size(), 0)

    def test_items_on_nonempty_list(self):
        test_stack = Stack()
        test_stack.push(10)
        test_stack.push(True)
        test_stack.push('Van')
        test_stack.push('Darkholme')
        test_stack.push(False)
        self.assertEqual(test_stack.items, [10, True, 'Van', 'Darkholme', False])

    def test_items_on_empty_list(self):
        test_stack = Stack()
        self.assertEqual(test_stack.items, [])

    def test_top_on_empty_list(self):
        with self.assertRaises(IndexError):
            test_stack = Stack()
            test_stack.top()


if __name__ == '__main__':
    main()
