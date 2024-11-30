# Maze Runner Game with
# - backtracking maze generator
# - manhattan distance heuristic
# - best first algorithm

from agent import Agent
from maze_generators import backtracking
from games import game
from heuristics import manhattan


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    best_first_path = agent.best_first(h)
    game.move_agent_in_maze(maze, best_first_path, "Manhattan Best First Random Maze Game")


def instantiate_problem(height, width):
    return backtracking.create_maze(height, width)


def h(cell_1, cell_2):
    return manhattan.manhattan_distance_heuristic(cell_1, cell_2)
