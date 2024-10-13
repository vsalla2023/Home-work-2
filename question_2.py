# -*- coding: utf-8 -*-
"""Question 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1us0ZWmf4976R_Mr4ZaXCC-P-h-hFR65-

**2. Dithering Algorithms: Floyd-Steinberg and Jarvis-Judice-Ninke**
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Floyd-Steinberg dithering function
def floyd_steinberg_dither(image):
    h, w = image.shape
    for y in range(h):
        for x in range(w):
            old_pixel = image[y, x]
            new_pixel = np.round(old_pixel / 255.0) * 255
            image[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            if x + 1 < w:
                image[y, x + 1] += quant_error * 7 / 16
            if x - 1 >= 0 and y + 1 < h:
                image[y + 1, x - 1] += quant_error * 3 / 16
            if y + 1 < h:
                image[y + 1, x] += quant_error * 5 / 16
            if x + 1 < w and y + 1 < h:
                image[y + 1, x + 1] += quant_error * 1 / 16
    return image

# Jarvis-Judice-Ninke dithering function
def jarvis_judice_ninke_dither(image):
    h, w = image.shape
    for y in range(h):
        for x in range(w):
            old_pixel = image[y, x]
            new_pixel = np.round(old_pixel / 255.0) * 255
            image[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            diffusion_matrix = [
                (1, 0, 7 / 48), (2, 0, 5 / 48),
                (-2, 1, 3 / 48), (-1, 1, 5 / 48), (0, 1, 7 / 48), (1, 1, 5 / 48), (2, 1, 3 / 48),
                (-2, 2, 1 / 48), (-1, 2, 3 / 48), (0, 2, 5 / 48), (1, 2, 3 / 48), (2, 2, 1 / 48)
            ]

            for dx, dy, diffusion_factor in diffusion_matrix:
                if 0 <= x + dx < w and 0 <= y + dy < h:
                    image[y + dy, x + dx] += quant_error * diffusion_factor
    return image

# Load image
image = cv2.imread('/content/image.jpg', 0)

# Apply Floyd-Steinberg dithering
fs_dithered = floyd_steinberg_dither(image.copy())

# Apply Jarvis-Judice-Ninke dithering
jjn_dithered = jarvis_judice_ninke_dither(image.copy())

# Show results
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.subplot(1, 3, 2), plt.imshow(fs_dithered, cmap='gray'), plt.title('Floyd-Steinberg')
plt.subplot(1, 3, 3), plt.imshow(jjn_dithered, cmap='gray'), plt.title('Jarvis-Judice-Ninke')
plt.show()

