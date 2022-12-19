def next_letter(letters, key):
    start = 0
    end = len(letters) - 1
    if key < letters[start] or key > letters[end]:
        return letters[0]

    while start <= end:
        mid = start + (end - start)//2

        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # start must be end + 1, so return start%len_arr
    return letters[start % len(letters)]


print(next_letter(['a', 'c', 'f', 'h'], 'b'))
