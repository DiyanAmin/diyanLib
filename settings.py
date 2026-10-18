'''
Changes/gets settings. (GLOBALLY)
'''

from . import data

_settings = data.json_handler('settings')

def save(do_import:bool = False,disable_tensorflow_warning:bool = True):
    _preferances = {
        'do_import':do_import,
        'disable_tensorflow_warning':disable_tensorflow_warning
    }
    _settings.save(_preferances)
def get():
    return _settings.get()