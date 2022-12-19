def remove_duplicates(arr):
    non_dup = 1
    i = 1
    result = [arr[0]]
    while i < len(arr):
        if arr[non_dup - 1] != arr[i]:
            arr[non_dup] = arr[i]
            result.append(arr[non_dup])
            non_dup += 1
        i += 1

    return result


print(remove_duplicates([2, 3, 3, 6, 6, 9]))
