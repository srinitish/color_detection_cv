import cv2
import numpy as np

def rgb_to_hsv_range(color):
    c = np.uint8([[color]])  # BGR input
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Extract hue value

    # Clamp hue between 0–179
    lower = np.array([max(hue - 10, 0), 100, 100], dtype=np.uint8)
    upper = np.array([min(hue + 10, 179), 255, 255], dtype=np.uint8)

    return lower, upper