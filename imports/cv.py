import cv2
from matplotlib import pyplot as plt
import numpy as np

def cv2_imshow(img): #For those of us who dont use colab.
    plt.imshow(img)
    plt.axis("off")
    plt.show()