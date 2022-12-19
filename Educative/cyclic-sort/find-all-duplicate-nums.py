def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:  # found duplicate
                print(nums)
                return nums[i]

        else:
            i += 1
    print(nums)
    return -1


print(find_duplicate([1, 4, 5, 3, 2]))
