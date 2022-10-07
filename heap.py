from copy import deepcopy

from typing import List, Generic, TypeVar, Callable

T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, data: List[T], comparator: Callable[[T, T], bool]):
        self.heap_array = data
        self.compare = comparator
        self.build()

    def build(self):
        last_non_leaf = len(self.heap_array) // 2 - 1
        for node_id in range(last_non_leaf, -1, -1):
            self.heapify(node_id)

    def heapify(self, node_id: int):
        left = self.left_child_id(node_id)
        right = self.right_child_id(node_id)

        optimal = node_id
        optimal = self.get_optimal(optimal, left)
        optimal = self.get_optimal(optimal, right)

        if optimal != node_id:
            self.swap_nodes(optimal, node_id)
            self.heapify(optimal)

    def optimal(self):
        return self.heap_array[0]

    def pop(self):
        optimal = self.heap_array[0]
        self.swap_nodes(0, len(self.heap_array) - 1)
        self.heap_array.pop()
        self.heapify(0)
        return optimal

    def swap_nodes(self, node_id_1: int, node_id_2: int):
        self.heap_array[node_id_1], self.heap_array[node_id_2] = self.heap_array[node_id_2], self.heap_array[node_id_1]

    def get_optimal(self, a: int, b: int) -> int:
        if not self.exists(b):
            return a
        return a if self.compare(self.heap_array[a], self.heap_array[b]) else b

    @staticmethod
    def left_child_id(node_id: int) -> int:
        return node_id * 2 + 1

    @staticmethod
    def right_child_id(node_id: int) -> int:
        return node_id * 2 + 2

    def exists(self, node_id: int) -> bool:
        return node_id < len(self.heap_array)

    def is_empty(self):
        return len(self.heap_array) == 0

    def sorted(self):
        result = []
        copied_heap = deepcopy(self)
        while not copied_heap.is_empty():
            result.append(copied_heap.pop())
        return result


class MinHeap(Heap[T]):
    def __init__(self, data: List[T]):
        super().__init__(data, lambda a, b: a < b)

    def min(self):
        return self.optimal()


class MaxHeap(Heap[T]):
    def __init__(self, data: List[T]):
        super().__init__(data, lambda a, b: a > b)

    def max(self):
        return self.optimal()
