#!/usr/bin/python3
import importlib.util
import dis

spec = importlib.util.spec_from_file_location('hidden_4', 'hidden_4.pyc')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# extract all names that meet the given criteria
names = []
for name in dir(module):
    if not name.startswith('__'):
        obj = getattr(module, name)
        if not callable(obj):
            names.append(name)

# print the names in alphabetical order
for name in sorted(names):
    print(name)
