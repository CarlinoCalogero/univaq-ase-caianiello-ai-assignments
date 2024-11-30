# A program which uses recursive backtracking to generate a maze

import random
import numpy as np
from directions import Directions
from maze import Maze


def create_maze(width, height, max_number_of_obstacles=None):
    # Figure out how many obstacle to create
    if max_number_of_obstacles is None:
        max_number_of_obstacles = width * height // 3

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
            # Set every cell of the outer layer of the maze as a wall
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                maze.maze[i, j] = 0  # create an obstacle

    for _ in range(max_number_of_obstacles):
        while True:
            i = random.randint(1, height - 2)
            j = random.randint(1, width - 2)
            if maze.maze[i, j] == 0:  # if there is already an obstacle others i and j
                continue
            maze.maze[i, j] = 0  # create an obstacle
            break  # object was created in a free cell so we can go creating a new one

    for i in range(height):
        for j in range(width):
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
            Directions.RIGHT.value: 0 if check_if_cell_is_outer_layer_cell(maze, cell_row, cell_column + 1) or
                                         maze.maze[
                                             cell_row, cell_column + 1] == 0 else 1,
        }


def check_if_cell_is_outer_layer_cell(maze, cell_row, cell_column):
    return cell_row == 0 or cell_row == maze.height - 1 or cell_column == 0 or cell_column == maze.width - 1
