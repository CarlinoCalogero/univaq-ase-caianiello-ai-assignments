def manhattan_distance_heuristic(cell_1, cell_2):
    """
    Computes the manhattan distance between the two cells

    :param cell_1: a cell of the maze expressed as a tuple
    :param cell_2: a cell of the maze expressed as a tuple
    :return:
    """
    x1, y1 = cell_1
    x2, y2 = cell_2

    return abs(x1 - x2) + abs(y1 - y2)
