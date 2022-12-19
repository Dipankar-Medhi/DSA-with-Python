# find the index of the minimum element.

"""
If arr[middle] > arr[middle + 1], then the element at middle + 1 is the smallest.
If arr[middle - 1] > arr[middle], then the element at middle is the smallest.
"""


def count_rotations(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start)//2

        # mid greater than next element
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1

        # mid is smaller than prev element
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # left side is sorted, so pivot is on right part
        if arr[start] < arr[mid]:
            start = mid + 1

        # right side is sorted, so pivot is on left side
        else:
            end = mid - 1
    return 0  # arr not rotated


print(count_rotations([10, 15, 1, 3, 8]))

# what if the array has duplicates


def count_rotations_with_duplicates(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start)//2

        # mid greater than next element
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1

        # mid is smaller than prev element
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        # skip one from start and end
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            # when start + 1 is not smallest
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            # element at end is not smallest
            if arr[end - 1] > arr[end]:
                return end
            end -= 1

        # left side is sorted, so pivot is on the right side
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1

    return 0
