import game


if __name__ == '__main__':
    maze = game.instantiate_problem(10, 10)
    agent = game.instantiate_agent(maze)
    game.move_agent_in_maze(agent, maze)
