# A program which uses randomness to generate a maze

import random
from maze_generators import generator


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
