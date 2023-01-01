import cv2
import numpy as np

#### Duckietown Sample Pictures
#lower_hsv = np.array([0, 50, 68])
#upper_hsv = np.array([14, 159, 255])
#### Duckietown Simulation 1
lower_hsv = np.array([15, 236, 0])
upper_hsv = np.array([26, 255, 255])
#### Duckietown Simulation 2
#lower_hsv = np.array([17, 136, 0])
#upper_hsv = np.array([44, 255, 255])
#### Real Robot
#lower_hsv = np.array([0, 50, 68])
#upper_hsv = np.array([14, 159, 255])


def preprocess(image_rgb: np.ndarray) -> np.ndarray:
    """Returns a 2D array"""
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    return mask
