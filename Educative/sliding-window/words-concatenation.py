def word_concatenation(s, words):

    word_freq = {}

    # store the word freq in a hashmap
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    result = []
    words_count = len(words)
    word_len = len(words[0])

    for i in range((len(s) - words_count * word_len) + 1):
        words_seen = {}

        for j in range(words_count):
            # move the window to the next index
            next_idx = i + j * word_len

            word = s[next_idx : next_idx + word_len]

            # break if the word is not needed
            if word not in word_freq:
                break

            # add the word to seen map
            if word not in words_seen:
                words_seen[word] = 0

            words_seen[word] += 1

            # break if word has higher freq than required
            if words_seen[word] > word_freq.get(word, 0):
                break

            # store the index if found all the words
            if j + 1 == words_count:
                result.append(i)

    return result


print(word_concatenation("catcatfoxfox", ["fox", "cat"]))
