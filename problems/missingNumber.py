def missingNumber(nums):

    # using cyclic sort for sorting the numsay
    index = 0

    while(index < len(nums)):
        correctIndex = nums[index]
        if(correctIndex < len(nums) and correctIndex != nums[correctIndex]):
            swap(nums, index, correctIndex)
        else:
            index += 1
    ans = 0
    for i in range(len(nums)):

        if (nums[0] != 0):
            return ans

        elif (nums[i] != i):
            ans = i

    return ans


def swap(nums, first, second):
    nums[first], nums[second] = nums[second], nums[first]


print(missingNumber([3, 0, 1]))
