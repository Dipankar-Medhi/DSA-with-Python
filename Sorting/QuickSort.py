# Quick Sort Algorithm


class QuickSort:
    def quickSort(self, nums):
        self.sort(nums, 0, len(nums) - 1)
        return nums

    # takes the array, lowest value and highest value
    def sort(self, nums, low, high):
        if low >= high:
            return

        s, e = low, high
        # get the mid of the array
        m = int(s + (e - s) / 2)
        # get the mid element
        p = nums[m]

        # while the start is less than or equal to the end
        while s <= e:

            # if the array is sorted, it won't swap
            # i.e the the left half is already sorted
            while nums[s] < p:
                s += 1
            # same for the other half
            while nums[e] > p:
                e -= 1

            # for start < end index, we swap them
            if s <= e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        # Now that the pivot is at correct index, we sort the two halfs
        self.sort(nums, low, e)
        self.sort(nums, s, high)


arr = [5, 4, 3, 2, 1, 9]
print(QuickSort().quickSort(arr))
