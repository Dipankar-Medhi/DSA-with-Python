def findStringAnagram(s, p):
    start = 0
    matched = 0
    char_freq = {}
    result = []

    # store the char freq of the pattern in the hashmap
    for char in p:
        char_freq[char] = char_freq.get(char, 0) + 1

    for end in range(len(s)):
        right_char = s[end]

        # increment matched for if found in charfreq
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:  # chars found
                matched += 1

        # all chars found --> store the start index of the window
        if matched == len(char_freq):
            result.append((start, end))

        if end >= len(p) - 1:
            left_char = s[start]
            start += 1
            if left_char in char_freq:

                # if already found, then reduce the matched cause
                # it is being removed, and it is no more found.
                if char_freq[left_char] == 0:
                    matched -= 1

                # considering the outgoing element as present in the map
                # for future window events. So that it is taken as found.
                char_freq[left_char] += 1

    return result


print("Start and End indexes: ", findStringAnagram("abbcabc", "abc"))
