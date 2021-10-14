def cyclicSort(arr):
    index = 0

    while(index < len(arr)):
        correctIndex = arr[index] - 1
        if(arr[index] != arr[correctIndex]):
            swap(arr, index, correctIndex)
        else:
            index += 1

    return arr


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


print(cyclicSort([3, 5, 2, 1, 4, 7, 6]))
