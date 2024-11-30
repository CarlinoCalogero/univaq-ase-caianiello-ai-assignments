from games import manhattan_best_first_random_maze_game, manhattan_a_star_random_maze_game, manhattan_best_first_backtracked_maze_game, manhattan_a_star_backtracked_maze_game, euclidean_best_first_random_maze_game, euclidean_a_star_random_maze_game, euclidean_best_first_backtracked_maze_game, euclidean_a_star_backtracked_maze_game, wall_following_backtracked_maze_game

if __name__ == '__main__':
    maze_height = 10
    maze_width = 10

    # Wall following
    wall_following_backtracked_maze_game.play(maze_height, maze_width)

    # Euclidean distance heuristic
    euclidean_best_first_random_maze_game.play(maze_height, maze_width)
    euclidean_a_star_random_maze_game.play(maze_height, maze_width)
    euclidean_best_first_backtracked_maze_game.play(maze_height, maze_width)
    euclidean_a_star_backtracked_maze_game.play(maze_height, maze_width)

    # Manhattan distance heuristic
    manhattan_best_first_random_maze_game.play(maze_height, maze_width)
    manhattan_a_star_random_maze_game.play(maze_height, maze_width)
    manhattan_best_first_backtracked_maze_game.play(maze_height, maze_width)
    manhattan_a_star_backtracked_maze_game.play(maze_height, maze_width)
