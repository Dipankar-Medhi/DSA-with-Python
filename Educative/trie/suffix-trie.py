class SuffixTrie:
    def __init__(self, string) -> None:
        self.root = {}
        self.end = "*"
        self.populate(string)

    # o(n2) time | O(n2) space
    def populate(self, string):
        for i in range(len(string)):
            self.insertAt(i, string)

    def insertAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            # letter not in the dict
            if letter not in node:
                node[letter] = {}
            # letter is present
            node = node[letter]
        node[self.end] = True

        print(node)

    # o(n) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]

        return self.end in node


trie = SuffixTrie("ababc")
trie.populate("bab")
print(trie.contains("bab"))
