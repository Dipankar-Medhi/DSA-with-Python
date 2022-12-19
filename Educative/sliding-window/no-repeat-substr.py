def noRepeatSubstr(s):
    start = 0
    max_len = 0
    char_index_map = {}

    for end in range(len(s)):
        right_char = s[end]

        if right_char in char_index_map:
            start = max(start, char_index_map[right_char] + 1)

        char_index_map[right_char] = end

        max_len = max(max_len, end - start + 1)

    return max_len


print(noRepeatSubstr('aabccbb'))
