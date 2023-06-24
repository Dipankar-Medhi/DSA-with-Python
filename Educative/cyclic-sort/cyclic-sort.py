# Time complexity = O(n)
# algorithm interats oer the array once.

def cyclicSort(arr):
    i = 0
    while i < len(arr):
        # correct index
        j = arr[i] - 1

        if arr[i] != arr[j]:
            # swap them
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    return arr


def main():
    print(cyclicSort([1, 4, 5, 3, 2]))


main()
