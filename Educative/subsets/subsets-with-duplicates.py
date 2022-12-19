def find_subsets(nums):
    # sort the arr
    nums.sort()

    subsets = []
    subsets.append([])

    start, end = 0, 0

    for i in range(len(nums)):
        start = 0
        # if curr and prev element are same, then add curr num to only the subset added in prev step
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1

        end = len(subsets) - 1

        for j in range(start, end + 1):
            # create a new subset by adding the curr element
            new_subset = list(subsets[j])
            new_subset.append(nums[i])
            subsets.append(new_subset)

    return subsets


print(find_subsets([1, 2, 2]))
