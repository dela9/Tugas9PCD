# -*- coding: utf-8 -*-
"""Tugas9PCD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M_jd5Bmg9x8ky0tVwC9x-hVgRQ49wW-j
"""

import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np

img = iio.imread("/content/kucing.jpeg", mode='F')

robertX = np.array([
    [1, 0],
    [0, -1]
])

robertY = np.array([
    [0, 1],
    [-1, 0]
])

sobelX = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobelY = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

def apply_filter(img, kernel):
    imgpad = np.pad(img, pad_width=((kernel.shape[0]//2, kernel.shape[0]//2),
                                    (kernel.shape[1]//2, kernel.shape[1]//2)), mode='constant')
    output = np.zeros_like(img)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            region = imgpad[y:y+kernel.shape[0], x:x+kernel.shape[1]]
            output[y, x] = np.sum(region * kernel)
    return output

Gx_robert = apply_filter(img, robertX)
Gy_robert = apply_filter(img, robertY)
G_robert = np.sqrt(Gx_robert**2 + Gy_robert**2)
G_robert = (G_robert / G_robert.max()) * 255
G_robert = G_robert.astype(np.uint8)

Gx_sobel = apply_filter(img, sobelX)
Gy_sobel = apply_filter(img, sobelY)
G_sobel = np.sqrt(Gx_sobel**2 + Gy_sobel**2)
G_sobel = (G_sobel / G_sobel.max()) * 255
G_sobel = G_sobel.astype(np.uint8)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title("Robert Gx")
plt.imshow(Gx_robert, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title("Robert Gy")
plt.imshow(Gy_robert, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title("Sobel Gx")
plt.imshow(Gx_sobel, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("Sobel Gy")
plt.imshow(Gy_sobel, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title("Robert Magnitude")
plt.imshow(G_robert, cmap='gray')
plt.axis('off')

plt.show()

plt.figure(figsize=(6, 6))
plt.title("Sobel Magnitude")
plt.imshow(G_sobel, cmap='gray')
plt.axis('off')
plt.show()