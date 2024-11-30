# A program which uses recursive backtracking to generate a maze

import random
import sys
from maze_generators import generator
from domain.directions import Directions

sys.setrecursionlimit(8000)


def create_maze(init_width, init_height):
    # Generate a maze object
    maze = generator.generate_maze_base_object(init_width, init_height)

    for i in range(maze.height):
        for j in range(maze.width):
            # Sets all odd rows and columns cells to 0 (black)
            # This will give the desired alternating pattern of a grid
            if i % 2 == 1 or j % 2 == 1:
                maze.maze[i, j] = 0
            # Set every cell of the outer layer of the maze as a visited node
            if i == 0 or j == 0 or i == maze.height - 1 or j == maze.width - 1:
                maze.maze[i, j] = 0.5  # we mark visited cells with 0.5 (gray)

    # Select a random cell as starting point for the generator
    # The starting cell must be an unvisited cell and not a wall or an outer layer part of the maze
    sx = random.choice(range(2, maze.width - 2, 2))
    sy = random.choice(range(2, maze.height - 2, 2))

    backtracking_algorithm(sx, sy, maze.maze)

    for i in range(maze.height):
        for j in range(maze.width):
            # Change the path color from gray to white
            if maze.maze[i, j] == 0.5:
                maze.maze[i, j] = 1
            # Compute maze map for cells
            generator.compute_maze_map_cell_entry(maze, i, j)
            # Compute maze grid
            if not generator.check_if_cell_is_outer_layer_cell(maze, i, j):
                maze.grid.append((i, j))

    generator.generate_start_and_goal_cells(maze)

    return maze


def backtracking_algorithm(cx, cy, grid):
    """
    Backtracking algorithm implementation

    :param cx: current x location that the algorithm is at
    :param cy: current y location that the algorithm is at
    :param grid: grid the algorithm is in
    :return:
    """

    # mark current location as visited. We have grid[cy, cx] and not grid[cx, cy] due to how numpy defines its
    # axes. Axis 0 is the rows of the array, which means it’s the height. Axis 1 is the columns of the array,
    # which means it’s the width.
    grid[cy, cx] = 0.5

    # check if there are any adjacent cells to visit or not
    if grid[cy - 2, cx] == 0.5 and grid[cy + 2, cx] == 0.5 and grid[cy, cx - 2] == 0.5 and grid[cy, cx + 2] == 0.5:
        # if we are surrounded on all sides by visited cells then do nothing
        pass
    else:
        # if there is a path through then we randomly choose a direction, and continue going that way
        li = [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value, Directions.RIGHT.value]
        while len(li) > 0:
            direction = random.choice(li)
            li.remove(direction)

            # if we are traveling upwards, the new empty cell to go to is located 2 units above (cy) and the wall
            # to carve through is 1 unit above (my). Since we are moving in the up direction, we do not need to
            # change the x values.
            if direction == Directions.UP.value:
                ny = cy - 2
                my = cy - 1
            elif direction == Directions.DOWN.value:
                ny = cy + 2
                my = cy + 1
            else:
                ny = cy
                my = cy

            if direction == Directions.LEFT.value:
                nx = cx - 2
                mx = cx - 1
            elif direction == Directions.RIGHT.value:
                nx = cx + 2
                mx = cx + 1
            else:
                nx = cx
                mx = cx

            # check if this randomly selected adjacent cell is visited or not
            if grid[ny, nx] != 0.5:
                # If this randomly selected adjacent cell is visited, then go and select another cell to move to
                grid[my, mx] = 0.5
                backtracking_algorithm(nx, ny, grid)

            # If this randomly selected adjacent cell is not visited, then carve the wall, and then do the same
            # process, this time on the new cell
