def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0  # if we ar emoving forward or not
        slow, fast = i, i

        # if slow or fast becomes -1, then we cannot find cycle for this element
        while True:
            # slow move one step
            slow = find_next_index(arr, is_forward, slow)
            # fast move one step
            fast = find_next_index(arr, is_forward, fast)

            if fast != -1:
                # move fast another step
                fast = find_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(arr, is_forward, curr_index):
    direction = arr[curr_index] >= 0
    if is_forward != direction:
        return -1  # change in direct

    next_index = (curr_index + arr[curr_index]) % len(arr)

    # one element cycle return -1
    if next_index == curr_index:
        next_index = -1

    return next_index


print(circular_array_loop_exists([1, 2, -1, 2, 2]))
