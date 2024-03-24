from unittest import TestCase, main
from stack.main import Stack


class TestStack(TestCase):

    def test_instance(self):
        some_list = []
        test_stack = Stack(some_list)
        self.assertIsInstance(test_stack.stack, list)

    def test_push_first(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(5)
        self.assertEqual(test_stack.items(), [5])

    def test_push_second(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(10)
        test_stack.push('Billy')
        test_stack.pop()
        self.assertEqual(test_stack.size(), 1)

    def test_push_third(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(10)
        test_stack.push('Billy')
        test_stack.push('Van')
        self.assertEqual(test_stack.items(), [10, 'Billy', 'Van'])

    def test_push_fourth(self):
        with self.assertRaises(AttributeError):
            some_list = 1
            test_stack = Stack(some_list)
            test_stack.push(1)

    def test_push_fifth(self):
        with self.assertRaises(AttributeError) as e:
            some_list = 'sfsa'
            test_stack = Stack(some_list)
            test_stack.push(1)
        self.assertEqual(e.exception.args[0], 'Добавить можем только в список :(')

    def test_pop_first(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(10)
        test_stack.push('Billy')
        test_stack.push('Van')
        test_stack.pop()
        test_stack.pop()
        self.assertEqual(test_stack.items(), [10])

    def test_pop_second(self):
        with self.assertRaises(IndexError):
            some_list = []
            test_stack = Stack(some_list)
            test_stack.pop()

    def test_pop_third(self):
        with self.assertRaises(IndexError) as e:
            some_list = []
            test_stack = Stack(some_list)
            test_stack.pop()
        self.assertEqual(e.exception.args[0], 'В списке должно должен быть хотя бы один элемент')

    def test_is_empty_first(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(5)
        self.assertEqual(test_stack.is_empty(), False)

    def test_is_empty_second(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(5)
        test_stack.pop()
        self.assertEqual(test_stack.is_empty(), True)

    def test_is_empty_third(self):
        with self.assertRaises(TypeError):
            some_list = 5
            test_stack = Stack(some_list)
            test_stack.is_empty()

    def test_is_empty_fourth(self):
        with self.assertRaises(TypeError) as e:
            some_list = 'Billy'
            test_stack = Stack(some_list)
            test_stack.is_empty()
        self.assertEqual(e.exception.args[0], 'Наличие элементов можем проверить только у списка')

    def test_size_first(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(5)
        test_stack.push(4)
        test_stack.push(3)
        test_stack.push(1)
        self.assertEqual(test_stack.size(), 4)

    def test_size_second(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(5)
        test_stack.pop()
        self.assertEqual(test_stack.size(), 0)

    def test_size_third(self):
        with self.assertRaises(TypeError):
            some_list = 5
            test_stack = Stack(some_list)
            test_stack.size()

    def test_size_fourth(self):
        with self.assertRaises(TypeError) as e:
            some_list = 'Billy'
            test_stack = Stack(some_list)
            test_stack.size()
        self.assertEqual(e.exception.args[0], 'Размер стэка проверить можем только у списка')


    def test_items_first(self):
        some_list = []
        test_stack = Stack(some_list)
        test_stack.push(10)
        test_stack.push(True)
        test_stack.push('Van')
        test_stack.push('Darkholme')
        test_stack.push(False)
        self.assertEqual(test_stack.items(), [10, True, 'Van', 'Darkholme', False])

    def test_items_second(self):
        some_list = []
        test_stack = Stack(some_list)
        self.assertEqual(test_stack.items(), [])

    def test_top_first(self):
        with self.assertRaises(IndexError):
            some_list = []
            test_stack = Stack(some_list)
            test_stack.top()

    def test_top_second(self):
        with self.assertRaises(IndexError) as e:
            some_list = []
            test_stack = Stack(some_list)
            test_stack.top()
        self.assertEqual(e.exception.args[0], 'В списке должно должен быть хотя бы один элемент')


if __name__ == '__main__':
    main()
