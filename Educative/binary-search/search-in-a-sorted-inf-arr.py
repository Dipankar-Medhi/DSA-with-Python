import math


class ArrReader:
    def __init__(self, arr) -> None:
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf

        return self.arr[index]


def search(reader, key):
    # find the correct bound
    start, end = 0, 1
    # when key not in bound
    while reader.get(end) < key:
        newStart = end + 1
        end += end - start + 1
        # double the bound size
        start = newStart

    # when key found in the bound
    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start)//2
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:  # key == reader.get(mid)
            return mid

    return -1


reader = ArrReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search(reader, 11))

# time O(logn) + O(logn) = O(logn)
# space is O(1)
