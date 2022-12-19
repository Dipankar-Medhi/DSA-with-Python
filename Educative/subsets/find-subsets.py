
def find_subsets(nums):

    subsets = []
    # add empty [] to subset
    subsets.append([])

    for num in nums:
        # insert the num on all existing subsets
        for i in range(len(subsets)):
            new_subset = list(subsets[i])
            new_subset.append(num)
            subsets.append(new_subset)

    return subsets


print(find_subsets([1, 2, 3]))

# time and space is O(2^n)

# Backtracking solution


def find_subsets2(nums):
    subsets = []
    backtrack(nums, 0, [], subsets)
    return subsets


def backtrack(nums, index, track, subsets):
    # add the initial track copy
    subsets.append(track.copy())
    # for every element on arr
    for i in range(index, len(nums)):
        # add to the track
        track.append(nums[i])
        # then move down the recursion tree
        backtrack(nums, i + 1, track, subsets)
        # remove the track when returning upwards on the tree
        track.remove(nums[i])


print(find_subsets2([1, 3, 5]))
