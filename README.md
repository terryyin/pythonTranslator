pythonTranslator
================

This project is going to provide multiple language support for the Python programming language. e.g. Enable Python to output error messages in Chinese.

My current plan is to use
sys.displayhook(value)
and
sys.excepthook(type, value, traceback)
to add hooks to Python. Then probably use
$PYTHONSTARTUP
To make it default behavior of the system.