# We need to turn pip index back on because Anaconda turns
# it off for some reason.
set PIP_NO_INDEX=False
set PIP_NO_DEPENDENCIES=False
set PIP_IGNORE_INSTALLED=False

"%PYTHON%" -m pip install pyvideoreader -vv
if errorlevel 1 exit 1