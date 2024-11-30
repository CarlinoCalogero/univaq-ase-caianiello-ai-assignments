# Maze Runner Game with
# - backtracking maze generator
# - Euclidean distance heuristic
# - A* algorithm

from domain.agent import Agent
from maze_generators import backtracking
from games import game
from heuristics import euclidean


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    a_star_path = agent.a_star(h)
    game.move_agent_in_maze(maze, a_star_path, "Euclidean A* Random Maze Game")


def instantiate_problem(height, width):
    return backtracking.create_maze(height, width)


def h(cell_1, cell_2):
    return euclidean.euclidean_distance_heuristic(cell_1, cell_2)
