import pandas as pd
import numpy as np
import seaborn as sb

import keras

from matplotlib import pyplot as plt

from keras.layers import Dense,Flatten,Dropout,Conv2D,MaxPooling2D
from keras.models import Sequential
from keras.datasets import mnist,cifar10
from keras.constraints import MaxNorm
import keras.utils as ku
from keras.optimizers import SGD

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression,LinearRegression