# A program which uses randomness to generate a maze

import random
from maze_generators import generator
from domain.agent import Agent
from heuristics import manhattan
import math
from domain.directions import Directions


def create_maze(init_width, init_height, max_number_of_obstacles=None):
    # Figure out how many obstacle to create
    if max_number_of_obstacles is None:
        max_number_of_obstacles = init_width * init_height // 3

    # Generate a maze object
    maze = generator.generate_maze_base_object(init_width, init_height)

    for i in range(maze.height):
        for j in range(maze.width):
            # Set every cell of the outer layer of the maze as a wall
            if i == 0 or j == 0 or i == maze.height - 1 or j == maze.width - 1:
                maze.maze[i, j] = 0  # create an obstacle

    randomized_algorithm(maze, max_number_of_obstacles)

    generator.generate_start_and_goal_cells(maze)

    tweak_maze(maze)

    return maze


def randomized_algorithm(maze, max_number_of_obstacles):
    for _ in range(max_number_of_obstacles):
        while True:
            i = random.randint(1, maze.height - 2)
            j = random.randint(1, maze.width - 2)
            if maze.maze[i, j] == 0:  # if there is already an obstacle others i and j
                continue
            maze.maze[i, j] = 0  # create an obstacle
            break  # object was created in a free cell, so we can go creating a new one

    for i in range(maze.height):
        for j in range(maze.width):
            # Compute maze map for cells
            generator.compute_maze_map_cell_entry(maze, i, j)
            # Compute maze grid
            if not generator.check_if_cell_is_outer_layer_cell(maze, i, j):
                maze.grid.append((i, j))


def tweak_maze(maze):
    while True:
        agent = Agent(maze)
        agent.a_star(manhattan.manhattan_distance_heuristic)

        # Check if maze has blocked goal
        if check_if_maze_has_blocked_goal(agent):
            # Get the closest cell to goal
            closest_cell = find_cell_closest_to_goal(agent)

            # define wall cell to break
            wall_cell_to_break = maze.start_cell

            # explore all four neighbours
            for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                              Directions.RIGHT.value]:
                # check if there is a wall in current selected direction
                if maze.maze_map[closest_cell][direction] == 0:
                    neighbour_cell = maze.start_cell

                    # find neighbour wall cell to break
                    if direction == Directions.UP.value:
                        neighbour_cell = (closest_cell[0] - 1, closest_cell[1])

                    if direction == Directions.DOWN.value:
                        neighbour_cell = (closest_cell[0] + 1, closest_cell[1])

                    if direction == Directions.RIGHT.value:
                        neighbour_cell = (closest_cell[0], closest_cell[1] + 1)

                    if direction == Directions.LEFT.value:
                        neighbour_cell = (closest_cell[0], closest_cell[1] - 1)

                    if not generator.check_if_cell_is_outer_layer_cell(maze, neighbour_cell[0], neighbour_cell[1]):
                        wall_cell_to_break_goal_cell_distance = compute_cell_distance(wall_cell_to_break, maze.goal_cell)
                        neighbour_cell_goal_cell_distance = compute_cell_distance(neighbour_cell, maze.goal_cell)
                        if neighbour_cell_goal_cell_distance < wall_cell_to_break_goal_cell_distance:
                            wall_cell_to_break = neighbour_cell

            if wall_cell_to_break != maze.start_cell:
                # Carve a path in the wall
                maze.maze[wall_cell_to_break[0], wall_cell_to_break[1]] = 1
                generator.compute_maze_map_cell_entry(maze, wall_cell_to_break[0], wall_cell_to_break[1])
                # Recompute for neighbour cells
                generator.compute_maze_map_cell_entry(maze, wall_cell_to_break[0] - 1, wall_cell_to_break[1])  # UP
                generator.compute_maze_map_cell_entry(maze, wall_cell_to_break[0] + 1, wall_cell_to_break[1])  # DOWN
                generator.compute_maze_map_cell_entry(maze, wall_cell_to_break[0], wall_cell_to_break[1] - 1)  # LEFT
                generator.compute_maze_map_cell_entry(maze, wall_cell_to_break[0], wall_cell_to_break[1] + 1)  # RIGHT
        else:
            break


def check_if_maze_has_blocked_goal(agent):
    return agent.maze.goal_cell not in agent.states


def find_cell_closest_to_goal(agent):
    closest_cell = agent.maze.start_cell
    for child_cell in agent.states:
        parent_cell = agent.states[child_cell]

        child_cell_goal_cell_distance = compute_cell_distance(child_cell, agent.maze.goal_cell)
        parent_cell_goal_cell_distance = compute_cell_distance(parent_cell, agent.maze.goal_cell)

        nearest_cell_goal_cell_distance = compute_cell_distance(closest_cell, agent.maze.goal_cell)

        if child_cell_goal_cell_distance < nearest_cell_goal_cell_distance:
            closest_cell = child_cell

        if parent_cell_goal_cell_distance < nearest_cell_goal_cell_distance:
            closest_cell = parent_cell

    return closest_cell


def compute_cell_distance(cell_1, cell_2):
    return math.sqrt((cell_2[0] - cell_1[0]) ** 2 + (cell_2[1] - cell_1[1]) ** 2)
