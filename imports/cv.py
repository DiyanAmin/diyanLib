import cv2
from matplotlib import pyplot as plt
import numpy as np

def cv2_imshow(img):
    plt.imshow(img)
    plt.axis("off")
    plt.show()