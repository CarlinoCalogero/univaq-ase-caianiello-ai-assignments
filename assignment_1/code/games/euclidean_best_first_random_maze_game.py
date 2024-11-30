# Maze Runner Game with
# - randomized maze generator
# - Euclidean distance heuristic
# - best first algorithm

from agent import Agent
from maze_generators import randomized
from games import game
from heuristics import euclidean


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    best_first_path = agent.best_first(h)
    game.move_agent_in_maze(maze, best_first_path, "Euclidean Best First Random Maze Game")


def instantiate_problem(height, width):
    return randomized.create_maze(height, width)


def h(cell_1, cell_2):
    return euclidean.euclidean_distance_heuristic(cell_1, cell_2)
