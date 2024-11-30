from queue import PriorityQueue
from domain.directions import Directions
import copy


class Agent:

    def __init__(self, maze):
        self.__maze = maze

    @property
    def maze(self):
        return self.__maze

    @maze.setter
    def maze(self, maze):
        self.__maze = maze

    # Best First algorithm implementation
    def best_first(self, h):
        # Initialize all grid cells heuristic distance to the goal to infinite
        f_score = {cell: float('inf') for cell in self.__maze.grid}
        # set the heuristic distance to the goal of the start cell
        f_score[self.__maze.start_cell] = h(self.__maze.start_cell, self.__maze.goal_cell)

        # create a priority queue
        open = PriorityQueue()
        # put the start cell to the priority queue
        # every cell in the priority queue has as first priority h()+g() and as second priority only h()
        open.put((h(self.__maze.start_cell, self.__maze.goal_cell), self.__maze.start_cell))

        # create the dictionary to store the path where children are the keys and their parents are the value
        child_key_parent_value_path = {}

        # loop until priority queue is empty
        while not open.empty():
            current_cell = open.get()[1]  # minimum value cell
            # check if current_cell is the goal
            if current_cell == self.__maze.goal_cell:
                break  # end the computation

            # explore all four neighbours
            for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                              Directions.RIGHT.value]:
                # check if there is a path in current select direction
                if self.__maze.maze_map[current_cell][direction]:  # 1 is equal to True
                    # define current cell
                    child_cell = (0, 0)

                    # find neighbour cell
                    if direction == Directions.UP.value:
                        child_cell = (current_cell[0] - 1, current_cell[1])
                    if direction == Directions.DOWN.value:
                        child_cell = (current_cell[0] + 1, current_cell[1])
                    if direction == Directions.RIGHT.value:
                        child_cell = (current_cell[0], current_cell[1] + 1)
                    if direction == Directions.LEFT.value:
                        child_cell = (current_cell[0], current_cell[1] - 1)

                    # compute new f score
                    temp_f_score = h(child_cell, self.__maze.goal_cell)

                    # check if new f score is less than previous f score
                    if temp_f_score < f_score[child_cell]:
                        # update the f score of the child cell
                        f_score[child_cell] = temp_f_score
                        # add entry to priority queue
                        open.put((h(child_cell, self.__maze.goal_cell), child_cell))
                        # add node to path
                        child_key_parent_value_path[child_cell] = current_cell

        # create the dictionary to store the path where children are the value and parents the key
        return self.reverse_path(child_key_parent_value_path, self.__maze.goal_cell, [])

    # A* algorithm implementation
    def a_star(self, h):
        # Initialize all grid cells distance from start cell to infinite
        g_score = {cell: float('inf') for cell in self.__maze.grid}
        # the distance from start cell of the start cell is 0
        g_score[self.__maze.start_cell] = 0

        # Initialize all grid cells heuristic distance to the goal to infinite
        f_score = {cell: float('inf') for cell in self.__maze.grid}
        # set the heuristic distance to the goal of the start cell
        f_score[self.__maze.start_cell] = h(self.__maze.start_cell, self.__maze.goal_cell)

        # create a priority queue
        open = PriorityQueue()
        # put the start cell to the priority queue
        # every cell in the priority queue has as first priority h()+g() and as second priority only h()
        open.put((
            h(self.__maze.start_cell, self.__maze.goal_cell) + 0, h(self.__maze.start_cell, self.__maze.goal_cell),
            self.__maze.start_cell))

        # create the dictionary to store the path where children are the keys and their parents are the value
        child_key_parent_value_path = {}

        # loop until priority queue is empty
        while not open.empty():
            current_cell = open.get()[2]  # minimum value cell
            # check if current_cell is the goal
            if current_cell == self.__maze.goal_cell:
                break  # end the computation

            # explore all four neighbours
            for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                              Directions.RIGHT.value]:
                # check if there is a path in current select direction
                if self.__maze.maze_map[current_cell][direction]:  # 1 is equal to True
                    # define current cell
                    child_cell = (0, 0)

                    # find neighbour cell
                    if direction == Directions.UP.value:
                        child_cell = (current_cell[0] - 1, current_cell[1])
                    if direction == Directions.DOWN.value:
                        child_cell = (current_cell[0] + 1, current_cell[1])
                    if direction == Directions.RIGHT.value:
                        child_cell = (current_cell[0], current_cell[1] + 1)
                    if direction == Directions.LEFT.value:
                        child_cell = (current_cell[0], current_cell[1] - 1)

                    # compute new g score
                    temp_g_score = g_score[current_cell] + 1

                    # compute new f score
                    temp_f_score = temp_g_score + h(child_cell, self.__maze.goal_cell)

                    # check if new f score is less than previous f score
                    if temp_f_score < f_score[child_cell]:
                        # update the g score and the f score of the child cell
                        g_score[child_cell] = temp_g_score
                        f_score[child_cell] = temp_f_score
                        # add entry to priority queue
                        open.put((temp_f_score, h(child_cell, self.__maze.goal_cell), child_cell))
                        # add node to path
                        child_key_parent_value_path[child_cell] = current_cell

        # create the dictionary to store the path where children are the value and parents the key
        return self.reverse_path(child_key_parent_value_path, self.__maze.goal_cell)

    def wall_follower(self):
        """
        Implementation of the Left Wall Following Algorithm.
        It finds a solution only if the maze has a path to the goal.

        :return:
        """

        # Set start cell as current cell
        current_cell = self.__maze.start_cell
        # Set up the direction dictionary of the agent.
        # Agent moves from top to bottom, so its direction is pointing down
        direction_dictionary = {
            Directions.UP.name: Directions.DOWN.value,
            Directions.LEFT.name: Directions.RIGHT.value,
            Directions.DOWN.name: Directions.UP.value,
            Directions.RIGHT.name: Directions.LEFT.value
        }
        # Create the array for storing the path and put the current cell inside it
        path = [current_cell]

        while True:
            # Check if goal was reached
            if current_cell == self.__maze.goal_cell:
                break
            # Check if there is a wall on the left side
            if self.__maze.maze_map[current_cell][direction_dictionary[Directions.LEFT.name]] == 0:
                # Check if there is a wall on the front side
                if self.__maze.maze_map[current_cell][direction_dictionary[Directions.UP.name]] == 0:
                    # Rotate clock wise
                    direction_dictionary = self.rotate_clock_wise(direction_dictionary)
                else:
                    current_cell = self.move_forward(current_cell, direction_dictionary)
                    path.append(current_cell)
            else:
                # Rotate counter clock wise
                direction_dictionary = self.rotate_counter_clock_wise(direction_dictionary)
                current_cell = self.move_forward(current_cell, direction_dictionary)
                path.append(current_cell)

        return path

    def dfs(self):
        # Create the list of explored cells
        explored = [self.__maze.start_cell]
        # Create the list of frontier cells
        frontier = [self.__maze.start_cell]

        # create the dictionary to store the path where children are the keys and their parents are the value
        child_key_parent_value_path = {}

        # loop until the frontier is not empty
        while len(frontier) > 0:
            # Get current cell
            current_cell = frontier.pop()
            # Check if goal was reached
            if current_cell == self.__maze.goal_cell:
                break
            # Explore each of the directions and find child cells
            for direction in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value,
                              Directions.RIGHT.value]:
                # Check if the path is open
                if self.__maze.maze_map[current_cell][direction]:
                    # Create a child cell
                    child_cell = (0, 0)

                    # find the child cell
                    if direction == Directions.RIGHT.value:
                        child_cell = (current_cell[0], current_cell[1] + 1)
                    elif direction == Directions.LEFT.value:
                        child_cell = (current_cell[0], current_cell[1] - 1)
                    elif direction == Directions.DOWN.value:
                        child_cell = (current_cell[0] + 1, current_cell[1])
                    elif direction == Directions.UP.value:
                        child_cell = (current_cell[0] - 1, current_cell[1])

                    # Check if child cell was already explored
                    if child_cell in explored:
                        # Skip to next direction
                        continue

                    # Add child cell to explored list
                    explored.append(child_cell)

                    # Add child cell to frontier list
                    frontier.append(child_cell)

                    # Add the cells to the path
                    child_key_parent_value_path[child_cell] = current_cell

        # create the dictionary to store the path where children are the value and parents the key
        return self.reverse_path(child_key_parent_value_path, self.__maze.goal_cell, [])


    def rotate_clock_wise(self, direction_dictionary):
        keys = list(direction_dictionary.keys())
        values = list(direction_dictionary.values())
        # rotate values
        rotated_values = [values[-1]]+values[:-1]
        # update the values of the keys
        return dict(zip(keys, rotated_values))

    def rotate_counter_clock_wise(self, direction_dictionary):
        keys = list(direction_dictionary.keys())
        values = list(direction_dictionary.values())
        # rotate values
        rotated_values = values[1:]+[values[0]]
        # update the values of the keys
        return dict(zip(keys, rotated_values))

    def move_forward(self, current_cell, direction_dictionary):
        """
        Moves the agent one step forward

        :param current_cell: current position of the agent in the maze
        :return:
        """
        if direction_dictionary[Directions.UP.name] == Directions.RIGHT.value:
            return (current_cell[0], current_cell[1] + 1)
        if direction_dictionary[Directions.UP.name] == Directions.LEFT.value:
            return (current_cell[0], current_cell[1] - 1)
        if direction_dictionary[Directions.UP.name] == Directions.UP.value:
            return (current_cell[0] - 1, current_cell[1])
        if direction_dictionary[Directions.UP.name] == Directions.DOWN.value:
            return (current_cell[0] + 1, current_cell[1])

    def reverse_path(self, child_key_parent_value_path, current_cell, path=None):
        if path is None:
            path = []
        if self.__maze.start_cell == current_cell:
            path.append(current_cell)
            return path
        # Check if agent can never reach goal because path is blocked
        if current_cell not in child_key_parent_value_path:
            return self.online_path(child_key_parent_value_path, path)
        next_cell = child_key_parent_value_path[current_cell]
        path = self.reverse_path(child_key_parent_value_path, next_cell, path)
        path.append(current_cell)
        return path

    def online_path(self, child_key_parent_value_path, path):
        # if dictionary is empty path is complete
        if not bool(child_key_parent_value_path):
            return path
        current_key = list(child_key_parent_value_path.keys())[0]
        current_cell = child_key_parent_value_path[current_key]
        # Check if path is empty
        if not path:
            # Set the cell as current position of the agent
            path.append(current_cell)
        elif path and path[len(path) - 1] != current_cell:  # Check if cell is not the current position of the agent
            # Check if current cell and previous cell are neighbours
            if not self.check_if_two_cells_are_neighbours(path[len(path) - 1], current_cell):
                # If the two cells are not neighbours make the agent go back to turning point
                self.compute_path_to_turning_point(path, current_cell)
            # Recheck if the last cell in path changed due to the previous instruction
            if path[len(path) - 1] != current_cell:
                # Set the cell as current position of the agent
                path.append(current_cell)
        path.append(current_key)
        child_key_parent_value_path_copy = copy.deepcopy(child_key_parent_value_path)
        del child_key_parent_value_path_copy[current_key]
        return self.online_path(child_key_parent_value_path_copy, path)

    def check_if_two_cells_are_neighbours(self, cell_1, cell_2):
        x_diff = abs(cell_1[0] - cell_2[0])
        y_diff = abs(cell_1[1] - cell_2[1])
        return (
                (not (x_diff == 1 and y_diff == 1)) and  # cells on diagonal are not considered neighbours
                (x_diff == 0 or x_diff == 1) and
                (y_diff == 0 or y_diff == 1)
        )

    def compute_path_to_turning_point(self, path, cell_next_to_turning_point_cell):
        backtracking_index = len(path) - 1
        while True:
            current_cell = path[backtracking_index]
            if current_cell != path[len(path) - 1]:
                path.append(current_cell)
            backtracking_index -= 1
            if backtracking_index < 0 or self.check_if_two_cells_are_neighbours(current_cell,
                                                                                cell_next_to_turning_point_cell):  # if they are neighbours backtracking path is completed
                return
