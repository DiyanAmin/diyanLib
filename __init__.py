#This file is the __init__.py file of diyanLib, created by Diyan Amin. It is available on Github.

do_import = False

print('Hello from Diyan Amin!')

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

print('Set environment variable to false.')

#Importing sub-modules
from . import data
print('Imported diyanLib.data')

settings = data.json_handler('settings')
preferences=settings.get()

if preferences.get('do_import'):
    from . import imports
    print('Imported diyanLib.imports')
else:
    print('Variable do_import is set to False. Set it to True using diyanLib.settings.save(do_import=True). Setting to false improves execution speed by NOT importing libraries')

from . import utils
print('Imported diyanLib.utils')

print('\n\nTrademark DiyanAmin 2026\nhttps://github.com/DiyanAmin/diyanLib\n\n')

#Trademark DiyanAmin 2026