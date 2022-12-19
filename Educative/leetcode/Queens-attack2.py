board = [
    ["o", "o", "o", "o"],
    ["o", "x", "o", "o"],
    ["o", "o", "x", "o"],
    ["x", "o", "o", "o"],
]

# lets start at (1, 2) i.e 2nd row, 3rd col


def countTheNumOfPossiblemoves(board):
    row = 3
    col = 1
    visited = set()
    res = {"count": 0}
    count = explore(board, row, col, visited, 0, res)
    return count


def explore(board, row, col, visited, count, res):
    rowInbound = 0 < row and row < len(board) - 1
    colInbound = 0 < col and col < len(board[0]) - 1

    if not rowInbound or not colInbound:
        return

    if (row, col) in visited:
        return

    if board[row][col] == "x":
        return

    visited.add((row, col))
    res["count"] += 1
    if rowInbound and colInbound:
        explore(board, row + 1, col, visited, count + 1, res)
        explore(board, row - 1, col, visited, count + 1, res)
        explore(board, row, col + 1, visited, count + 1, res)
        explore(board, row, col - 1, visited, count + 1, res)
        explore(board, row + 1, col + 1, visited, count + 1, res)
        explore(board, row - 1, col - 1, visited, count + 1, res)

    return res


print(countTheNumOfPossiblemoves(board))
