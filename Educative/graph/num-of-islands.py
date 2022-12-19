## Time O(row*cols) == space


def islandCount(grid):
    count = 0
    visited = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                count += 1

    return count


def explore(grid, row, col, visited):
    # matrix bounds
    rowInbound = 0 <= row and row < len(grid)
    colInbound = 0 <= col and col < len(grid[0])
    if not rowInbound or not colInbound:
        return False

    if grid[row][col] == "w":
        return False

    if (row, col) in visited:
        return False

    visited.add((row, col))
    # look top and bottom
    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    # look left and right
    explore(grid, row, col - 1, visited)
    explore(grid, row, col + 1, visited)

    return True


grid = [
    ["w", "l", "w", "w"],
    ["w", "l", "l", "w"],
    ["w", "w", "l", "w"],
    ["l", "w", "w", "l"],
]
print(islandCount(grid))
