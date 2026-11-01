#This file is the __init__.py file of diyanLib, created by Diyan Amin. It is available on Github.

do_import = False

print('Hello from Diyan Amin!')

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

#Importing sub-modules
from . import data
settings = data.json_handler('settings')
preferences=settings.get()

if preferences.get('do_import'):
    from . import imports

from . import utils
#Trademark DiyanAmin 2026