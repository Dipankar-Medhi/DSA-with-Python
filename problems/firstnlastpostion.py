def searchRange(nums, target: int):
    ans = [-1, -1]

    if target not in nums:
        return ans
    start = search(nums, target, True)
    end = search(nums, target, False)
    ans[0] = start
    ans[1] = end

    return ans


def search(nums, target: int, findStart: bool):

    pot_ans = -1
    start = 0
    end = len(nums) - 1

    while(start <= end):

        mid = int(start + (end - start)/2)

        if (target < nums[mid]):
            end = mid - 1
        elif(target > nums[mid]):
            start = mid + 1
        else:
            pot_ans = mid
            if(findStart):
                end = mid - 1
            else:
                start = mid + 1

    return pot_ans


print(searchRange([5, 7, 7, 8, 8, 10], 8))
