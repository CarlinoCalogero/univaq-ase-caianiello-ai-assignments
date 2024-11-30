# A template for a Maze Runner Game module

from screen import display
import copy
import numpy as np


def play(height, width):
    pass


def instantiate_problem(height, width):
    pass


# Heuristic function
def h(cell_1, cell_2):
    pass


def move_agent_in_maze(maze, path, window_name):
    display.create_window(window_name)
    for cell in path:
        maze_copy = copy.deepcopy(maze.maze)

        # Create a 3D array for color image
        color_img = np.zeros((len(maze_copy), len(maze_copy[0]), 3), dtype=np.uint8)

        for i in range(len(maze_copy)):
            for j in range(len(maze_copy[0])):
                if i == cell[0] and j == cell[1]:
                    color_img[i, j] = (0, 0, 255)  # Red in BGR
                elif i == maze.start_cell[0] and j == maze.start_cell[1]:
                    color_img[i, j] = (0, 255, 0)  # Green in BGR
                elif i == maze.goal_cell[0] and j == maze.goal_cell[1]:
                    color_img[i, j] = (255, 0, 0)  # Blue in BGR
                elif maze_copy[i][j] == 1:
                    color_img[i, j] = (255, 255, 255)  # White in BGR
                elif maze_copy[i][j] == 0:
                    color_img[i, j] = (0, 0, 0)  # Black in BGR

        display.display(color_img, window_name)

    display.wait()
