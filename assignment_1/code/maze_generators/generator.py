from directions import Directions
from domain.maze import Maze
import numpy as np


def generate_maze_base_object(width, height):
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


def generate_start_and_goal_cells(maze):
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
    maze.maze[maze.height - 2, maze.width - 3] = 1
    maze.goal_cell = (maze.height - 2, maze.width - 3)
    # Recompute for neighbour cells
    compute_maze_map_cell_entry(maze, maze.height - 2, maze.width - 3)
    compute_maze_map_cell_entry(maze, maze.height - 2 - 1, maze.width - 3)  # UP
    compute_maze_map_cell_entry(maze, maze.height - 2 + 1, maze.width - 3)  # DOWN
    compute_maze_map_cell_entry(maze, maze.height - 2, maze.width - 3 - 1)  # LEFT
    compute_maze_map_cell_entry(maze, maze.height - 2, maze.width - 3 + 1)  # RIGHT
