#This file is the __init__.py file of diyanLib, created by Diyan Amin. It is available on Github.

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

#Importing sub-modules
from . import data
from . import imports
from . import utils

#Trademark DiyanAmin 2026