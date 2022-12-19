"""
- We will keep a running count of every matching instance of a character.
- Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.
- We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the window.
"""


def findSubstr(s, t):
    start, matched, substr_start = 0, 0, 0
    min_len = len(s) + 1
    char_freq = {}
    # store chars of pattern in a hashmap
    for char in t:
        char_freq[char] = char_freq.get(char, 0) + 1

    for end in range(len(s)):
        right_char = s[end]

        if right_char in char_freq:
            char_freq[right_char] -= 1
            # count every matching char
            if char_freq[right_char] >= 0:
                matched += 1
        # shrink the window if we can
        while matched == len(t):
            if min_len > end - start + 1:
                min_len = end - start + 1
                substr_start = start

            left_char = s[start]
            start += 1

            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    if min_len > len(s):
        return ""
    return s[substr_start: substr_start + min_len]


print(findSubstr("ADOBECODEBANC", "ABC"))
