def longestSubstring(s, k):
    max_len = 0
    start = 0
    char_freq = {}

    for end in range(len(s)):
        right_char = s[end]
        char_freq[right_char] = char_freq.get(right_char, 0) + 1

        if char_freq[right_char] >= k:
            max_len = max(max_len, end - start + 1)

    return max_len


print(longestSubstring("ababbc", 2))
