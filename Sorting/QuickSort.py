# Quick Sort Algorithm


class QuickSort:
    def quickSort(self, nums):
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, low, high):
        if low >= high:
            return

        s, e = low, high
        m = int(s + (e - s)/2)
        p = nums[m]

        while (s <= e):

            # if the array is sorted, it won't swap
            while (nums[s] < p):
                s += 1
            while (nums[e] > p):
                e -= 1

            if (s <= e):
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        # Now that the pivot is at correct index, we sort the two halfs
        self.sort(nums, low, e)
        self.sort(nums, s, high)


arr = [5, 4, 3, 2, 1]
print(QuickSort().quickSort(arr))
