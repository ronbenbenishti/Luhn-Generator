import sys, platform
from cx_Freeze import setup, Executable

includefiles = ['luhn.ico']
includes = []
excludes = []
packages = []

def getTargetName():
    myOS = platform.system()
    if myOS == 'Linux':
        return "LuhnGen"
    elif myOS == 'Windows':
        return "Luhn Generator.exe"
    else:   
        return "Luhn.dmg"
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    script = "luhn.py",
    base = base,
    icon = "luhn.ico",
    )

setup(
    name = "Luhn Number Generator",
    version = "1.0",
    description = "Luhn Number Generator",
    author = "Ron Benbenishti",
    targetName = getTargetName(),
    executables = [exe],
    options = {'build_exe': {'includes':includes,'packages':packages,'include_files':includefiles}},
    copyright = 'Copyright (C) Ron Benbenishti'
    )
