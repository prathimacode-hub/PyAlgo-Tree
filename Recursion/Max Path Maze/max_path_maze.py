"""A script to demonstrate recursion in Python.
The script shows a recursive function to check 
how many available paths there are from a given
starting point to the end of the maze,
the most bottem-right cell."""

# Check if cell is valid or not
def valid_cell(x, y):
    return not(x < 0 or y < 0 or x >= length or y >= length)

# Main recursion function
def count_valid_paths(maze, x, y, checked, paths):
    # Base case, if "end" is found, increment by 1
    if x == length - 1 and y == length - 1:
        return paths + 1

    checked[x][y] = True

    # If the current cell is valid and open
    # we start recursing all posible directions
    if valid_cell(x, y) and maze[x][y] == 1:
        if x + 1 < length and not checked[x + 1][y]:
            paths = count_valid_paths(maze, x + 1, y, checked, paths)
        
        if x - 1 >= 0 and not checked[x - 1][y]:
            paths = count_valid_paths(maze, x - 1, y, checked, paths)
        
        if y + 1 < length and not checked[x][y + 1]:
            paths = count_valid_paths(maze, x, y + 1, checked, paths)
        
        if y - 1 >= 0 and not checked[x][y - 1]:
            paths = count_valid_paths(maze, x, y - 1, checked, paths)

    # Backtrack from the cell and mark it as checked
    checked[x][y] = False
    return paths

# Driver code, the 2D array represents the maze
# 1 is open space, 0 is closed
if __name__ == '__main__':

    maze = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1,]
    ]

    length = len(maze)

    # counter for the paths
    paths = 0

    # Create 2D matrix to keep track of cells visited
    checked = [[False for x in range(length)] for y in range(length)]

    paths = count_valid_paths(maze, 0, 0, checked, paths)

    print("There are " + str(paths) + " paths through the maze")     # Should print 4 initially
