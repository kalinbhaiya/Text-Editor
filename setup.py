import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Mudasir\AppData\Local\Programs\Python\Python38\tcl\tcl8.6" #You may have differet path
os.environ['TK_LIBRARY'] = r"C:\Users\Mudasir\AppData\Local\Programs\Python\Python38\tcl\tk8.6"   #You may have different path

executables = [cx_Freeze.Executable("Viper.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Viper Text Editor", # name Application
    options = {"build_exe": {"packages":["tkinter","os","webbrowser"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}}, #Go to DLLs folder and copy the files('tcl86t.dll', 'tk86t.dll') and paste them in your current project directory
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
#to create the installer, open cmd in your project directory and run the following command:
#"python setup.py bdist_msi" for windows
#your exe installer will be created.
