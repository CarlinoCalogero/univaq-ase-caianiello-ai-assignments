import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import copy


def animate(maze, path, animated_video_name):
    # Create frames list
    frames = []

    for cell in path:
        # Copy the maze
        maze_copy = copy.deepcopy(maze.maze)

        # Create a 3D array for color image
        color_img = np.zeros((len(maze_copy), len(maze_copy[0]), 3), dtype=np.uint8)

        for i in range(len(maze_copy)):
            for j in range(len(maze_copy[0])):
                if i == cell[0] and j == cell[1]:
                    color_img[i, j] = (0, 0, 255)  # Red in BGR
                elif i == maze.start_cell[0] and j == maze.start_cell[1]:
                    color_img[i, j] = (0, 255, 0)  # Green in BGR
                elif i == maze.goal_cell[0] and j == maze.goal_cell[1]:
                    color_img[i, j] = (255, 0, 0)  # Blue in BGR
                elif maze_copy[i][j] == 1:
                    color_img[i, j] = (255, 255, 255)  # White in BGR
                elif maze_copy[i][j] == 0:
                    color_img[i, j] = (0, 0, 0)  # Black in BGR

        frames.append(copy.deepcopy(color_img))

    # Create a figure and axes
    figure, axes = plt.subplots()
    image = axes.imshow(frames[0], cmap='brg')  # Use 'brg' colormap for BGR
    animated_video = animation.FuncAnimation(figure, update_image, frames=len(frames), fargs=(image, frames), interval=500, blit=True)
    animated_video.save(animated_video_name, writer='ffmpeg', fps=5)
    plt.show()


def update_image(i, image, frames):
    image.set_data(frames[i])
    return image,