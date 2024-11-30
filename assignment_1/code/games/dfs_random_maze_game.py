# Maze Runner Game with
# - randomized maze generator
# - DFS algorithm

from domain.agent import Agent
from maze_generators import randomized
from games import game
from heuristics import euclidean


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    dfs_path = agent.dfs()
    game.move_agent_in_maze(maze, dfs_path, "DFS Random Maze Game")


def instantiate_problem(height, width):
    return randomized.create_maze(height, width)


def h(cell_1, cell_2):
    return euclidean.euclidean_distance_heuristic(cell_1, cell_2)
