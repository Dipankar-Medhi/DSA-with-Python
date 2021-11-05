def findDuplicate(nums):  # nums = [1,3,4,2,2]
    index = 0

    while(index < len(nums)):
        correctIndex = nums[index] - 1
        if(nums[index] != nums[correctIndex]):
            swap(nums, index, correctIndex)
        else:
            index += 1

    ans = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            ans.append(nums[i])

    return ans[0]


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


print(findDuplicate([1, 1, 2]))
