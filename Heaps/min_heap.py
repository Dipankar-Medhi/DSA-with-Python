"""Implementing Minimunm Heap with an array list"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Sift the new value up to its correct position
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        # If the heap is empty, return None
        if not self.heap:
            return None
        # Remove the minimum value from the root of the heap
        min_value = self.heap[0]
        # Replace the root with the last value in the heap
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            # Sift the new root down to its correct position
            self._sift_down(0)
        return min_value

    def show(self):
        return self.heap

    def _sift_up(self, index):
        # Find the parent index of the node at index
        parent_index = (index - 1) // 2
        # If the parent value is greater than the node value, swap them
        if index > 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = (
                self.heap[index],
                self.heap[parent_index],
            )
            # Recursively sift the node up until it is in its correct position
            self._sift_up(parent_index)

    def _sift_down(self, index):
        # Find the indices of the left and right children of the node at index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        # Find the index of the minimum value among the node and its children
        min_index = index
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[min_index]
        ):
            min_index = left_child_index
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[min_index]
        ):
            min_index = right_child_index
        # If the minimum value is not the node itself, swap the node with the minimum value
        if index != min_index:
            self.heap[index], self.heap[min_index] = (
                self.heap[min_index],
                self.heap[index],
            )
            # Recursively sift the node down until it is in its correct position
            self._sift_down(min_index)


min_heap = MinHeap()
min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)

print("Minimum heap:", min_heap.show())

print("Minimum value:", min_heap.extract_min())
