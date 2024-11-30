# In order to install cv2 type
# pip install opencv-python
import cv2


def create_window(window_name):
    print("Using OpenCV version: " + cv2.__version__)
    cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)


def display(image, window_name):
    cv2.imshow(window_name, image)
    cv2.waitKey(300)


def close_window():
    cv2.destroyAllWindows()


def wait():
    cv2.waitKey(0)
    close_window()
