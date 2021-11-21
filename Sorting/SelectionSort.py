def selectionSort(arr):
    for i in range(len(arr)):
        # find the max element in the remaining arr and swap with the correct index
        # for finding the last element
        lastIndex = len(arr) - i - 1
        # for finding the index of mex element
        maxIndex = getMaxIndex(arr, lastIndex)
        # swapping the last index element with the max element
        swap(arr, maxIndex, lastIndex)
    return arr


def getMaxIndex(arr, end):
    max = 0
    for i in range(end+1):
        if arr[i] > arr[max]:
            max = i
    return max


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


arr = [3, 4, 1, 6, 2]
print(selectionSort(arr))
