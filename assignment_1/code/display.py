import cv2


def create_window():
    print("Using OpenCV version: " + cv2.__version__)

    cv2.namedWindow('Maze', cv2.WINDOW_KEEPRATIO)


def display(image):
    cv2.imshow('Maze', image)
    cv2.waitKey(500)

    # cv2.imwrite(self.path, self._maze * 255.0)


def close_window():
    cv2.destroyAllWindows()


def wait():
    cv2.waitKey(0)
