def noRepeatSubstr(s):
    start = 0
    max_len = 0
    char_index_map = {} # store the most recent index of the chars

    for end in range(len(s)):
        right_char = s[end]

        if right_char in char_index_map:
            start = max(start, char_index_map[right_char] + 1)
            #For each character, we check if it already exists in the char_map dictionary and if its index is greater than or equal to the current start pointer.

            # If it does, it means the character is repeated within the current substring. In this case, we move the start pointer to the next position after the repeated character to exclude it from the new substring.

        char_index_map[right_char] = end

        max_len = max(max_len, end - start + 1)

    return max_len


print(noRepeatSubstr('aabccbb'))
