"""Implementing max heap with array list"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)
        # Sift the new value up to its correct position
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        # If the heap is empty, return None
        if not self.heap:
            return None
        # Remove the maximum value from the root of the heap
        max_value = self.heap[0]
        # Replace the root with the last value in the heap
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            # Sift the new root down to its correct position
            self._sift_down(0)
        return max_value

    def show(self):
        return self.heap

    def _sift_up(self, index):
        # Find the parent index of the node at index
        parent_index = (index - 1) // 2
        # If the parent value is less than the node value, swap them
        if index > 0 and self.heap[parent_index] < self.heap[index]:
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
        # Find the index of the maximum value among the node and its children
        max_index = index
        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[max_index]
        ):
            max_index = left_child_index
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[max_index]
        ):
            max_index = right_child_index
        # If the maximum value is not the node itself, swap the node with the maximum value
        if index != max_index:
            self.heap[index], self.heap[max_index] = (
                self.heap[max_index],
                self.heap[index],
            )
            # Recursively sift the node down until it is in its correct position
            self._sift_down(max_index)


max_heap = MaxHeap()
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(7)
max_heap.insert(1)

print("Maximum heap:", max_heap.show())

print("Maximum value:", max_heap.extract_max())
