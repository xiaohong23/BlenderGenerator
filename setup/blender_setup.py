import runpy
import bpy
import sys, os
import importlib

paths = ["D:\\Documents\\Cours\\UTBM\\S2\\IN55\\", "D:\\Documents\\Cours\\UTBM\\S2\\IN55\\BlenderGenerator"]
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

import BlenderGenerator.main
importlib.reload(BlenderGenerator.main)

BlenderGenerator.main.main()