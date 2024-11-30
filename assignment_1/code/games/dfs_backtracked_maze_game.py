# Maze Runner Game with
# - backtracking maze generator
# - DFS algorithm

from domain.agent import Agent
from maze_generators import backtracking
from games import game
from heuristics import euclidean


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    dfs_path = agent.dfs()
    game.move_agent_in_maze(maze, dfs_path, "DFS Backtracked Maze Game")


def instantiate_problem(height, width):
    return backtracking.create_maze(height, width)


def h(cell_1, cell_2):
    return euclidean.euclidean_distance_heuristic(cell_1, cell_2)
