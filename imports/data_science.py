import pandas as pd
import numpy as np
from numpy import argmax
import seaborn as sb

import keras

from matplotlib import pyplot as plt

from keras.layers import Dense,Flatten,Dropout,Conv2D,MaxPooling2D,Input
from keras.models import Sequential,load_model
from keras.datasets import mnist,cifar10
from keras.constraints import MaxNorm
from keras.utils import to_categorical,load_img,img_to_array
from keras.optimizers import SGD
from keras.preprocessing.image import load_img,img_to_array
from keras.metrics import Accuracy

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression,LinearRegression