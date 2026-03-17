import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_anomaly_otsu_mse(original, reconstructed, blur_kernel=(5, 5)):

    diff = np.abs(original - reconstructed)

    error_map = np.mean(diff, axis= -1)
    error_map_8unit = np.uint8(255 * error_map)

    # rozmycie Gausa
    blur = cv2.GaussianBlur(error_map_8unit,(5,5),0)

    # odpalenie otsu

    otsu_thresh_val, maska = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return otsu_thresh_val, maska, error_map

