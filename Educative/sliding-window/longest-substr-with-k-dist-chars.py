
def longestSubstrWithKDistinctChar(str, k):

    start = 0
    max_length = 0
    char_freq = {}

    for end in range(len(str)):
        right_char = str[end]
        # store the freq of the chars
        char_freq[right_char] = char_freq.get(right_char, 0) + 1

        # shrink the window for more than k distinct chars
        while len(char_freq) > k:
            left_char = str[start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            # shring the window
            start += 1
        # remember the max length so far
        max_length = max(max_length, end - start + 1)

    return max_length


print(longestSubstrWithKDistinctChar("cbbebi", 2))

# time complexity = O(N + N) --> for loop runs for all chars and while loop runs once for each chars
# space complexity = O(K) --> for storing K + 1 chars on hashmap
