### Wrong
visited = set()


def recurse(row, visited, col, board, index, word):
    if board[row][col] == word[index]:
        index += 1

    rowInbound = 0 <= row and row < len(board)
    colInbound = 0 <= col and col < len(board[0])
    if not rowInbound or not colInbound:
        return False

    if (row, col) in visited:
        return False

    if board[row][col] != word[index]:
        return False

    visited.add((row, col))
    # look top and bottom
    recurse(row - 1, visited, col, board, index + 1, word)
    recurse(row + 1, visited, col, board, index + 1, word)
    # left and right
    recurse(row, visited, col - 1, board, index + 1, word)
    recurse(row, visited, col + 1, board, index + 1, word)

    visited.remove((row, col))

    return True


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(recurse(0, visited, 0, board, 0, word))
