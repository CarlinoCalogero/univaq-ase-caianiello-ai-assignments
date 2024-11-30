class Maze:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__maze_map = {}
        self.__grid = []
        self.__maze = []
        self.__start_cell = (-1, -1)
        self.__goal_cell = (-1, -1)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def start_cell(self):
        return self.__start_cell

    @start_cell.setter
    def start_cell(self, start_cell):
        self.__start_cell = start_cell

    @property
    def goal_cell(self):
        return self.__goal_cell

    @goal_cell.setter
    def goal_cell(self, goal_cell):
        self.__goal_cell = goal_cell

    @property
    def maze_map(self):
        return self.__maze_map

    @maze_map.setter
    def maze_map(self, maze_map):
        self.__maze_map = maze_map

    @property
    def maze(self):
        return self.__maze

    @maze.setter
    def maze(self, maze):
        self.__maze = maze

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid
