from typing import Any, Self


class Stack:
    def __init__(self):
        self._stack: list[Any] = []

    def push(self, element: Any) -> Self:
        self._stack.append(element)
        return self

    def pop(self) -> Any:
        try:
            return self._stack.pop()
        except (IndexError):
            raise IndexError('В списке должно должен быть хотя бы один элемент')

    def is_empty(self) -> bool:
        return not self._stack

    def size(self) -> int:
        return len(self._stack)

    @property
    def items(self) -> list[Any]:
        some_list = self._stack.copy()
        return some_list

    def top(self) -> Any:
        try:
            return self._stack[-1]
        except (IndexError):
            raise IndexError('В списке должно должен быть хотя бы один элемент')