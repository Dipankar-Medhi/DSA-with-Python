"""
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
"""


def solution(s, k):
    start, max_len, max_repeat_count = 0, 0, 0
    freq = {}

    for end in range(len(s)):
        right_char = s[end]

        # add freq of chars in hashmap
        freq[right_char] = freq.get(right_char, 0) + 1

        # find max repeating count
        max_repeat_count = max(max_repeat_count, freq[right_char])

        # since we are not allowed to replace more than k chars, so the window is shrinked
        if (end - start + 1 - max_repeat_count) > k:
            left_char = s[start]
            freq[left_char] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


print(solution('abccde', 1))
