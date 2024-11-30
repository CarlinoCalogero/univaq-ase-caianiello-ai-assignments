# A program which uses recursive backtracking to generate a maze

import random
import numpy as np
import sys
from directions import Directions
from maze import Maze

sys.setrecursionlimit(8000)


def create_maze(width, height):
    # adjust the width and height for the grid in order to make sure that the maze's size, outer visited layer
    # included, are odd
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    # Create a maze object
    maze = Maze(height, width)

    # Creates a 2d array with all cells set at 1.0
    maze.maze = np.ones((height, width), dtype=float)

    for i in range(height):
        for j in range(width):
            # Sets all odd rows and columns cells to 0 (black)
            # This will give the desired alternating pattern of a grid
            if i % 2 == 1 or j % 2 == 1:
                maze.maze[i, j] = 0
            # Set every cell of the outer layer of the maze as a visited node
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                maze.maze[i, j] = 0.5  # we mark visited cells with 0.5 (gray)

    # Select a random cell as starting point for the generator
    # The starting cell must be an unvisited cell and not a wall or an outer layer part of the maze
    sx = random.choice(range(2, width - 2, 2))
    sy = random.choice(range(2, height - 2, 2))

    generator(sx, sy, maze.maze)

    for i in range(height):
        for j in range(width):
            # Change the path color from gray to white
            if maze.maze[i, j] == 0.5:
                maze.maze[i, j] = 1
            # Compute maze map for cells
            compute_maze_map_cell_entry(maze, i, j)
            # Compute maze grid
            if not check_if_cell_is_outer_layer_cell(maze, i, j):
                maze.grid.append((i, j))

    # Add the maze starting point
    maze.maze[1, 2] = 1
    maze.start_cell = (1, 2)
    compute_maze_map_cell_entry(maze, 1, 2)
    # Recompute for neighbour cells
    compute_maze_map_cell_entry(maze, 1 - 1, 2)  # UP
    compute_maze_map_cell_entry(maze, 1 + 1, 2)  # DOWN
    compute_maze_map_cell_entry(maze, 1, 2 - 1)  # LEFT
    compute_maze_map_cell_entry(maze, 1, 2 + 1)  # RIGHT

    # Add the goal
    maze.maze[height - 2, width - 3] = 1
    maze.goal_cell = (height - 2, width - 3)
    # Recompute for neighbour cells
    compute_maze_map_cell_entry(maze, height - 2, width - 3)
    compute_maze_map_cell_entry(maze, height - 2 - 1, width - 3)  # UP
    compute_maze_map_cell_entry(maze, height - 2 + 1, width - 3)  # DOWN
    compute_maze_map_cell_entry(maze, height - 2, width - 3 - 1)  # LEFT
    compute_maze_map_cell_entry(maze, height - 2, width - 3 + 1)  # RIGHT

    return maze


def generator(cx, cy, grid):
    """
    Backtracking algorithm implementation

    :param cx: current x location that the algorithm is at
    :param cy: current y location that the algorithm is at
    :param grid: grid the algorithm is in
    :return:
    """

    # mark current location as visited. We have grid[cy, cx] and not grid[cx, cy] due to how numpy defines its
    # axes. Axis 0 is the rows of the array, which means it’s the height. Axis 1 is the columns of the array,
    # which means it’s the width.
    grid[cy, cx] = 0.5

    # check if there are any adjacent cells to visit or not
    if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
        # if we are surrounded on all sides by visited cells then do nothing
        pass
    else:
        # if there is a path through then we randomly choose a direction, and continue going that way
        li = [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value, Directions.RIGHT.value]
        while len(li) > 0:
            direction = random.choice(li)
            li.remove(direction)

            # if we are traveling upwards, the new empty cell to go to is located 2 units above (cy) and the wall
            # to carve through is 1 unit above (my). Since we are moving in the up direction, we do not need to
            # change the x values.
            if direction == Directions.UP.value:
                ny = cy - 2
                my = cy - 1
            elif direction == Directions.DOWN.value:
                ny = cy + 2
                my = cy + 1
            else:
                ny = cy
                my = cy

            if direction == Directions.LEFT.value:
                nx = cx - 2
                mx = cx - 1
            elif direction == Directions.RIGHT.value:
                nx = cx + 2
                mx = cx + 1
            else:
                nx = cx
                mx = cx

            # check if this randomly selected adjacent cell is visited or not
            if grid[ny, nx] != 0.5:
                # If this randomly selected adjacent cell is visited, then go and select another cell to move to
                grid[my, mx] = 0.5
                generator(nx, ny, grid)

            # If this randomly selected adjacent cell is not visited, then carve the wall, and then do the same
            # process, this time on the new cell


def compute_maze_map_cell_entry(maze, cell_row, cell_column):
    # Remember that the outer layer does not count so the maze start at (1,1) and ends at (h-1, w-1)
    if (cell_row > 0 and cell_column > 0) and (cell_row < maze.height - 1 and cell_column < maze.width - 1):
        maze.maze_map[(cell_row, cell_column)] = {
            Directions.UP.value: 0 if check_if_cell_is_outer_layer_cell(maze, cell_row - 1, cell_column) or maze.maze[
                cell_row - 1, cell_column] == 0 else 1,
            Directions.DOWN.value: 0 if check_if_cell_is_outer_layer_cell(maze, cell_row + 1, cell_column) or maze.maze[
                cell_row + 1, cell_column] == 0 else 1,
            Directions.LEFT.value: 0 if check_if_cell_is_outer_layer_cell(maze, cell_row, cell_column - 1) or maze.maze[
                cell_row, cell_column - 1] == 0 else 1,
            Directions.RIGHT.value: 0 if check_if_cell_is_outer_layer_cell(maze, cell_row, cell_column + 1) or maze.maze[
                cell_row, cell_column + 1] == 0 else 1,
        }


def check_if_cell_is_outer_layer_cell(maze, cell_row, cell_column):
    return cell_row == 0 or cell_row == maze.height - 1 or cell_column == 0 or cell_column == maze.width - 1
