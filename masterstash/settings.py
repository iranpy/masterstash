import os
import sys
import importlib
from masterstash.utils import import_modules

class DifferSettings(object):
    def __init__(self):
        self._wrapped = None
    
    def _setup(self):
        self._wrapped = Setting()
    
    def __getattr__(self, name):
        if self._wrapped is None or os.environ.get('SETTINGS_CONF'):
            if os.environ.get('IS_SETTINGS_CONF'):
                del os.environ['IS_SETTINGS_CONF']
            self._setup()

        value = getattr(self._wrapped, name)
        self.__dict__[name] = value
        return value

    def __setattr__(self, name, value):
        """
        Set the value of setting. Clear all cached values if _wrapped changes
        or clear single values when set.
        """
        if name == '_wrapped':
            self.__dict__["_wrapped"] = value
        else:
            if self._wrapped:
                self._setup()
            setattr(self._wrapped, name, value)

class Setting(object):
    def __init__(self):
        if os.environ.get('SETTINGS_CONF'):
            module = import_modules(globals(), os.environ.get('SETTINGS_CONF'), main_module='configs')
            mod = module
        else:
            self.settings_module_dir = 'masterstash.config'
            mod = importlib.import_module(self.settings_module_dir)

        for setting_item in dir(mod):
            setting_value = object.__getattribute__(mod, setting_item)
            object.__setattr__(self, setting_item, setting_value)

settings = DifferSettings()