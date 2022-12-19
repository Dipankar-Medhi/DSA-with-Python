## Iterative solution
from collections import deque


def find_perm(nums):
    res = []
    permutations = deque()
    permutations.append([])

    for num in nums:
        for _ in range(len(permutations)):
            old_perm = permutations.popleft()
            # create new perm by adding the num at every positin
            for i in range(len(old_perm)):
                new_perm = list(old_perm)
                new_perm.insert(i, num)

                if len(new_perm) == len(nums):
                    res.append(new_perm)
                else:
                    permutations.append(new_perm)
    return res


print(find_perm([1, 3, 5]))

## recursive solution
def gen_permutations(nums):
    result = []
    recursion(nums, 0, [], result)
    return result


def recursion(nums, index, curr_perm, result):
    if index == len(nums):
        result.append(curr_perm)
    else:
        # add num at every position
        for i in range(len(curr_perm) + 1):
            neww_perm = list(curr_perm)
            neww_perm.insert(i, nums[index])
            recursion(nums, index + 1, neww_perm, result)


print(gen_permutations([1, 3, 5]))


def find_permutations(nums):
    results = []
    backtrack(nums, results, [])
    return results


def backtrack(nums, results, track):
    if len(track) == len(nums):
        results.append(track.copy())
        return
    for i in range(len(nums)):
        # skip if element already present on the track
        if nums[i] in track:
            continue
        # add the element to the track
        track.append(nums[i])
        # move down on the tree
        backtrack(nums, results, track)
        # remove the last element while going up the recursion tree
        track.remove(nums[i])


print(find_permutations([1, 3, 5]))
