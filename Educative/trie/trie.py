# class Node:
#     def __init__(self) -> None:
#         self.key = None
#         self.value = None
#         self.children = {}


# class Trie:
#     def __init__(self) -> None:
#         self.root = Node()

#     def insert(self, word, value):
#         currentWord = word
#         currentNode = self.root

#         while len(currentWord) > 0:
#             char = currentWord[0]  # 1st character
#             if char in currentNode.children:
#                 currentNode = currentNode.children[char]  # move curr node forward
#                 currentWord = currentWord[1:]  # consider the remaining characters

#             else:
#                 newNode = Node()
#                 newNode.key = char

#                 if len(currentWord) == 1:
#                     newNode.value = value

#                 currentNode.children[char] = newNode
#                 currentNode = newNode
#                 currentWord = currentWord[1:]

#     def lookup(self, word):
#         currentWord = word
#         currentNode = self.root

#         while len(currentWord) > 0:
#             char = currentWord[0]  # 1st char

#             if char in currentNode.children:
#                 currentNode = currentNode.children[char]  # move node forward
#                 print(currentNode.key, end="-->")
#                 currentWord = currentWord[1:]
#             else:
#                 return "Not in trie"

#         if currentNode.value == None:
#             return "None"
#         return currentNode.value

#     def printAllNodes(self):
#         nodes = [self.root]
#         while len(nodes) > 0:
#             for letter in nodes[0].children:
#                 nodes.append(nodes[0].children[letter])

#             return nodes


# def makeTrie(words):
#     trie = Trie()
#     for word, value in words.items():
#         trie.insert(word, value)
#     return trie


# trie = makeTrie({"how": 4, "are": 20, "you": 3})

# print(trie.lookup("how"))
# print(trie.printAllNodes())


# ------------------------------------------ #

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            print("Current node:", current_node.__str__())
            current_node = current_node.children[char]
        current_node.end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Create a Trie object
trie = Trie()

# Insert some words into the trie
trie.insert("apple")
trie.insert("banana")
trie.insert("pear")
trie.insert("peach")

# Search for a word in the trie
print(trie.search("apple")) # True
print(trie.search("grape")) # False

# Check if a word starts with a given prefix
print(trie.starts_with("pe")) # True
print(trie.starts_with("gr")) # False