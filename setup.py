"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import sys


if sys.platform=="darwin":
    from setuptools import setup

    APP = ['P2PP.py']
    DATA_FILES = ['p2pp.ui']
    OPTIONS = {'argv_emulation': True,
               "iconfile": "icons/icon.icns",
               "includes": ['PyQt5._qt'],
               }

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app']
    )

else:
    import sys
    import version
    from cx_Freeze import setup, Executable

    includefiles = ["p2pp.ui", "icons/icon.ico"]
    excludes = ["tkinter"]

    build_exe_options = {"packages": ["os"], 'include_files': includefiles, "excludes": excludes}

    setup(name="p2pp",
          version=version.Version,
          description="P2PP - Palette 2 Post Processing tool for Prusa Slicer",
          options={"build_exe": build_exe_options},
          executables=[Executable("p2pp.py", base="Win32GUI", icon="icons/icon.ico")]
          )




