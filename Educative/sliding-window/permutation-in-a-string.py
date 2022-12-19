def find_permutation_in_string(s, p):
    start, matched = 0, 0
    freq = {}

    # store char freq of pattern in the hashmap
    for char in p:
        freq[char] = freq.get(char, 0) + 1

    for end in range(len(s)):
        right_char = s[end]

        if right_char in freq:
            freq[right_char] -= 1

            if freq[right_char] == 0:
                matched += 1

        if matched == len(freq):
            return True

        if end >= len(p) - 1:
            left_char = s[start]
            start += 1

            if left_char in freq:
                if freq[left_char] == 0:
                    matched -= 1
                freq[left_char] += 1

    return False


print(find_permutation_in_string('eidbaooo', 'ab'))
