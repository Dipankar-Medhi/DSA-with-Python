# return of start using binary search gives the answer

def ceilingOfNumber(arr, target):
    if (target > arr[6]):
        return -1
    ans = ceilingbinarySearch(arr, target)  # return the start
    return arr[ans]


# return index of smallest number > = target
def ceilingbinarySearch(arr, target):

    start = 0
    end = len(arr) - 1

    # what if the target element is greater than greatest element in arr

    while (start <= end):
        # find the middle element // mid = (start + end) / 2
        mid = int(start + (end - start)/2)

        if (target < arr[mid]):             # search on the 1st half
            end = mid - 1

        elif (target > arr[mid]):
            start = mid + 1                 # search on the 2nd half

        else:
            return mid

    return start


arr = [2, 3, 5, 9, 14, 16, 18]
target = 15

print(ceilingOfNumber(arr, target))
