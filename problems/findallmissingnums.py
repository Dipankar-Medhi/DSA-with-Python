

# nums = [4, 3, 2, 7, 8, 2, 3, 1]
def findDisappearedNumbers(nums):
    index = 0

    while(index < len(nums)):
        correctIndex = nums[index] - 1
        if(nums[index] != nums[correctIndex]):
            swap(nums, index, correctIndex)
        else:
            index += 1

    # find the incorrect numbers
    ans = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            ans.append(i+1)

    return nums


def swap(nums, first, second):
    nums[first], nums[second] = nums[second], nums[first]


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
