import backtracking
import display
from agent import Agent
import copy
import numpy as np
import random_maze


def instantiate_problem(height, width):
    return random_maze.create_maze(height, width)


def instantiate_agent(maze):
    return Agent(maze)


# Heuristic function
def h(cell_1, cell_2):
    """
    Computes the manhattan distance between the two cells

    :param cell_1: a cell of the maze expressed as a tuple
    :param cell_2: a cell of the maze expressed as a tuple
    :return:
    """
    x1, y1 = cell_1
    x2, y2 = cell_2

    return abs(x1 - x2) + abs(y1 - y2)


def move_agent_in_maze(agent, maze):
    a_star_path = agent.best_first(h)
    display.create_window()
    for cell in a_star_path:
        maze_copy = copy.deepcopy(agent.maze.maze)

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

        display.display(color_img)

    display.wait()
