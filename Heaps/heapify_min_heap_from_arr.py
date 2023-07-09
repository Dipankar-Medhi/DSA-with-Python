def heapify(arr, n, i):
    # Initialize smallest as root
    smallest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    # See if right child of root exists and is smaller than root
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, smallest)


def build_min_heap(arr):
    n = len(arr)

    # Build a min heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr


arr = [4, 10, 3, 5, 1]
heap = build_min_heap(arr)

print(heap)
