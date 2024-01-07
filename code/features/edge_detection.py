import os

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

img = cv.imread('pillar.png', cv.IMREAD_GRAYSCALE)
x, y = img.shape
edges = cv.Canny(img, 50, 100)

plt.imshow(edges)
plt.show()