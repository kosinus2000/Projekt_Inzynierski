import cv2
import numpy as np

def generate_picture(width = 500, height = 500):

    image = np.zeros((width, height, 3 ), np.uint8)