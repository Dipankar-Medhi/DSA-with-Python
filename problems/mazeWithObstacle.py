
def mazePath(p, maze, r, c):
    # row is the number of element in maze and
    # col is the number of element in maze[0]
    if r == len(maze)-1 and c == len(maze[0])-1:
        print(p)

    # if element is False, then return(break recursion)
    if maze[r][c] == False:
        return
    if r < len(maze)-1:
        mazePath(p+'D', maze, r+1, c)
    if c < len(maze) - 1:
        mazePath(p+'R', maze, r, c+1)


maze = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

mazePath("", maze, 0, 0)
