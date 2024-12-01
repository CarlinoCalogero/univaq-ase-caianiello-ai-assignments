# Maze Runner Game with
# - backtracking maze generator
# - Left Wall
# - Wall Following algorithm

from domain.agent import Agent
from maze_generators import randomized
from games import game
from heuristics import euclidean


def play(height, width):
    maze = instantiate_problem(height, width)
    agent = Agent(maze)
    wall_follower_path = agent.wall_follower()
    game.move_agent_in_maze(maze, wall_follower_path, "Wall Following Random Maze Game")


def instantiate_problem(height, width):
    return randomized.create_maze(height, width)


def h(cell_1, cell_2):
    return euclidean.euclidean_distance_heuristic(cell_1, cell_2)
