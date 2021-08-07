__author__ = "greenteamoe"
__status__ = "planning"
__description__ = "Project made with Qt Designer and PySide6"

# Import modules
import sys
import os
from cx_Freeze import setup, Executable
from cx_Freeze.dist import build_exe

# Create variables and folders so the application can run

build_exe_options = {"packages": ["os"], "includes": ["PySide6"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "PYBOX",
    version = "1.0.0",
    description = "ToolBox made in Python using PySide6",
    author = __author__,
    options={'build_exe': build_exe_options},
    executables = [Executable("main.py", base=base)]
)