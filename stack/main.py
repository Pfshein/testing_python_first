class Stack:
    def __init__(self, stack):
        self.stack = stack

    def push(self, element):
        try:
            return self.stack.append(element)
        except (AttributeError):
            raise AttributeError('Добавить можем только в список :(')

    def pop(self):
        try:
            return self.stack.pop()
        except (IndexError, AttributeError):
            raise IndexError('В списке должно должен быть хотя бы один элемент')

    def is_empty(self):
        if isinstance(self.stack, list):
            return self.stack == []
        else:
            raise TypeError('Наличие элементов можем проверить только у списка')

    def size(self):
        if isinstance(self.stack, list):
            return len(self.stack)
        else:
            raise TypeError('Размер стэка проверить можем только у списка')

    def items(self):
        return self.stack

    def top(self):
        try:
            return self.stack[-1]
        except (IndexError, TypeError):
            raise IndexError('В списке должно должен быть хотя бы один элемент')


some_list = 5
test_stack = Stack(some_list)


if __name__ == '__main__':
    test_stack.is_empty()
