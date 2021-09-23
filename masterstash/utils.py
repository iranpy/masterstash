import importlib.util

def import_modules(context, path, main_module):
    spec = importlib.util.spec_from_file_location(main_module, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    context[main_module] = mod
    return context[main_module]